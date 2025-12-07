# Student Exam Score Regression - Python

Goal: Predict final exam score (G3) using study habits & demographic factors.  
Dataset: UCI Student Performance (395 rows, 33 features)

---

## Methods
- Data preprocessing & cleaning
- Exploratory data analysis (correlation heatmap, feature plots)
- Simple vs. multiple linear regression
- Train-test evaluation using scikit-learn

---

## Results
| Model | R² Score |
|------|----------|
| Simple Regression | -0.018 |
| Multiple Regression | 0.708 |

- Previous grades were the strongest predictors

---

## Visuals

Correlation Heatmap: [Correlation Heatmap](student_scores_regression_plots/correlation_heatmap.png)

Study Time vs Final Grade: [Study Time vs Final Grade](student_scores_regression_plots/StudyTimevsFinalGrade.png)

Feature Importance: [Feature Importance](student_scores_regression_plots/FeatureImportance.png)

Actual vs Predicted: [Actual vs Predicted](student_scores_regression_plots/ActualvsPredicted.png)
