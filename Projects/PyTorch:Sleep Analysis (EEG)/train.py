import os
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import f1_score, cohen_kappa_score
from sklearn.metrics import classification_report, confusion_matrix

class SleepDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


class RawCNN(nn.Module):
    def __init__(self, n_classes=5, in_channels=1):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv1d(in_channels, 16, kernel_size=50, stride=6), # 0.5 s kernel
            nn.BatchNorm1d(16),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=8),
            nn.Conv1d(16, 32, kernel_size=7, padding=3),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=4),
        )
        self.time_pool = nn.AdaptiveAvgPool1d(1)
        self.classifier = nn.Linear(32, n_classes)

    def forward(self, x):                   # x: (batch, 1, 3000)
        x = self.features(x)                # (batch, 32, 15)
        x = self.time_pool(x)               # (batch, 32, 1)
        x = x.flatten(1)                    # (batch, 32)
        return self.classifier(x)           # (batch, 5) logits

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")

X = np.load(os.path.join(data_dir, "X_subjnorm.npy"))
y = np.load(os.path.join(data_dir, "y.npy"))
subjects = np.load(os.path.join(data_dir, "subjects.npy"))

print(X.shape, y.shape, subjects.shape)

rng = np.random.default_rng(seed=123)

unique_subjects = np.unique(subjects)
shuffled = rng.permutation(unique_subjects)

train_subjects = set(shuffled[:20].tolist())
val_subjects = set(shuffled[20:25].tolist())
test_subjects = set(shuffled[25:].tolist())

train_idx = []
val_idx = []
test_idx = []

for i in range(len(subjects)):
    if subjects[i] in train_subjects:
        train_idx.append(i)
    elif subjects[i] in val_subjects:
        val_idx.append(i)
    else:
        test_idx.append(i)

X_train, y_train = X[train_idx], y[train_idx]
X_val, y_val = X[val_idx], y[val_idx]
X_test, y_test = X[test_idx], y[test_idx]

print("train:", sorted(train_subjects))
print("val:", sorted(val_subjects))
print("test:", sorted(test_subjects))
print(X_train.shape, X_val.shape, X_test.shape)
print(np.bincount(y_train), np.bincount(y_val), np.bincount(y_test))

train_dataset = SleepDataset(X_train, y_train)
val_dataset = SleepDataset(X_val, y_val)
test_dataset = SleepDataset(X_test, y_test)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size = 256, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=256, shuffle=False)

x_batch, y_batch = next(iter(train_loader))
print(x_batch.shape, y_batch.shape, x_batch.dtype, y_batch.dtype)
print(len(train_dataset), len(val_dataset), len(test_dataset))

torch.manual_seed(123)
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

model = RawCNN().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

x_batch, y_batch = next(iter(train_loader))
x_batch, y_batch = x_batch.to(device), y_batch.to(device)

def train_one_epoch(model, loader, loss_fn, optimizer):
    model.train()
    total_loss = 0.0
    total_count = 0

    for x, y in loader:
        x = x.to(device)
        y = y.to(device)

        optimizer.zero_grad()
        logits = model(x)
        loss = loss_fn(logits, y)
        loss.backward()
        optimizer.step()

        total_loss += loss.item() * len(y)
        total_count += len(y)

    return total_loss / total_count

def evaluate(model, loader, loss_fn):
    model.eval()
    total_loss = 0.0
    total_count = 0.0
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device)
            y = y.to(device)

            logits = model(x)
            loss = loss_fn(logits, y)
            total_loss += loss.item() * len(y)
            total_count += len(y)

            preds = logits.argmax(dim=1)
            all_preds.extend(preds.cpu().tolist())
            all_labels.extend(y.cpu().tolist())

    avg_loss = total_loss / total_count
    macro_f1 = f1_score(all_labels, all_preds, average="macro")
    kappa = cohen_kappa_score(all_labels, all_preds)

    return avg_loss, macro_f1, kappa, all_labels, all_preds

n_train_epochs = 20
best_f1 = 0.0
model_path = os.path.join(script_dir, "best_model_subjnorm.pt")

TRAIN = True

if TRAIN:
    for epoch in range(n_train_epochs):
        train_loss = train_one_epoch(model, train_loader, loss_fn, optimizer)
        val_loss, val_f1, val_kappa, _, _= evaluate(model, val_loader, loss_fn)

        print(f"Epoch {epoch + 1:2d} | train loss {train_loss:.3f} | "
            f"val loss {val_loss:.3f} | val F1 {val_f1:.3f} | kappa {val_kappa:.3f}")

        if val_f1 > best_f1:
            best_f1 = val_f1
            torch.save(model.state_dict(), model_path)

model.load_state_dict(torch.load(model_path))
_, _, _, all_labels, all_preds = evaluate(model, val_loader, loss_fn)
print(classification_report(all_labels, all_preds,
                            target_names=["W", "N1", "N2", "N3", "REM"]))
print(confusion_matrix(all_labels, all_preds))