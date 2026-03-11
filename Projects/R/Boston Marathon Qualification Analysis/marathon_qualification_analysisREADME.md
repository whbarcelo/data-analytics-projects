# Boston Marathon Qualification Analysis - R + ggplot2
Goal: Analyze Boston Marathon qualification trends across 1,081,649 runners from 762 qualifying races between 2022 and 2024.  
Dataset: Kaggle (Race-level finisher results, race metadata, BAA qualification standards by age and gender bracket)

---
## Methods
- Filtered and joined three datasets to produce a clean analytical dataset of 532 valid qualifying races
- Calculated yearly qualification rates and median finish times by gender and age group using dplyr
- Identified top qualifying races among events with 500+ finishers
- Fit three logistic regression models (age, gender, year) with model comparison via AIC and chi-square tests
- Fit a mixed effects logistic regression with a random intercept for race using lme4
- Tested an age × gender interaction term and visualized predicted qualification probabilities
- Evaluated final model on a held-out test set with confusion matrix, precision, recall, F1, and ROC curve
- Visualized all results using ggplot2 and knitted to PDF via R Markdown

---
## Models
| # | Model | Features |
|---|-------|----------|
| 1 | Logistic Regression | Age + Gender |
| 2 | Logistic Regression | Age + Age² + Gender |
| 3 | Logistic Regression | Age + Age² + Gender + Year |
| 4 | Mixed Effects Logistic Regression | Age + Age² + Gender + Year + (1\|Race) |
| 5 | Interaction Model | Age × Gender + Age² + Year |

---
## Results
| Metric | Value |
|--------|-------|
| Overall Qualification Rate | 13.7% |
| Qualification Rate 2022 | 11.8% |
| Qualification Rate 2024 | 14.6% |
| Median Finish Time Drop (2022–2024) | 7 minutes |
| Final Model AUC (held-out test set) | 0.569 |
| Race Random Intercept Variance | 0.96 |

- Qualification rates rose steadily from 2022 to 2024, accompanied by faster median finish times across all groups
- Older runners qualify at higher rates due to more lenient age-graded BAA standards, confirmed by logistic regression
- The age × gender interaction was not statistically significant (p = 0.118), suggesting the age effect is consistent across genders
- The mixed effects model reveals substantial race-level variation, confirming course selection is a key factor beyond demographics
- The top qualifying race (Highwayman Dash) had a qualification rate exceeding 75%, far above the overall average
- The majority of non-qualifiers missed their standard by 30+ minutes, suggesting the BQ standard is a hard ceiling for most runners

---
## Visuals
Rmd Knit: [Marathon Qualification Analysis](marathon_qualification_analysis.pdf)
