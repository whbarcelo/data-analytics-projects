import mne
import os
import numpy as np

from mne.datasets.sleep_physionet.age import fetch_data

mne.set_log_level("WARNING")

files = fetch_data(subjects=list(range(30)), recording=[1])

annotation_to_id = {
    "Sleep stage W": 1,
    "Sleep stage 1": 2,
    "Sleep stage 2": 3,
    "Sleep stage 3": 4,
    "Sleep stage 4": 4,
    "Sleep stage R": 5,
}
# Modern AASM standard merges stages 3 and 4 into one stage
event_id = {"W": 1, "N1": 2, "N2": 3, "N3": 4, "REM": 5}

sleep_stages = set(annotation_to_id) - {"Sleep stage W"}

def load_windows(psg_path, hyp_path):
    raw = mne.io.read_raw_edf(psg_path, stim_channel="Event marker",
                              infer_types=True, preload=True)
    annotations = mne.read_annotations(hyp_path)

    first_sleep_onset = None
    last_sleep_end = None
    for annot in annotations:
        if annot["description"] in sleep_stages:
            if first_sleep_onset is None:
                first_sleep_onset = annot["onset"]
            last_sleep_end = annot["onset"] + annot["duration"]

    annotations.crop(first_sleep_onset - 30 * 60, last_sleep_end + 30 * 60)
    raw.set_annotations(annotations, emit_warning=False)

    events, _ = mne.events_from_annotations(raw, event_id=annotation_to_id,
                                            chunk_duration=30.0)

    tmax = 30.0 - 1.0 / raw.info["sfreq"]
    epochs = mne.Epochs(raw, events, event_id=event_id, tmin=0.0, tmax=tmax,
                        baseline=None, picks=["Fpz-Cz"], preload=True)

    X = epochs.get_data()                   # (n_windows, 1, 3000)
    y = epochs.events[:, 2] - 1             # labels 0-4
    return X, y

X_list = []
y_list = []
subject_list = []

for psg_path, hyp_path in files:
    filename = os.path.basename(psg_path)
    subject_id = int(filename[3:5])         # "00" -> 0

    X_s, y_s = load_windows(psg_path, hyp_path)
    X_s = (X_s - X_s.mean()) / X_s.std()

    X_list.append(X_s)
    y_list.append(y_s)
    subject_list.append(np.full(len(y_s), subject_id))

X = np.concatenate(X_list)
X = X.astype(np.float32)
y = np.concatenate(y_list)
subjects = np.concatenate(subject_list)

print(X.shape, y.shape, subjects.shape)
print(np.unique(subjects, return_counts=True))
print(np.bincount(y))

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")

os.makedirs(data_dir, exist_ok=True)
np.save(os.path.join(data_dir, "X_subjnorm.npy"), X)
np.save(os.path.join(data_dir, "y.npy"), y)
np.save(os.path.join(data_dir, "subjects.npy"), subjects)