# Boston Marathon Qualification Analysis - R + ggplot2

**Goal:** Analyze Boston Marathon qualification trends across 1,071,822 runners from 530 qualifying race events (273 distinct races) between 2022 and 2024.

**Dataset:** Kaggle (race-level finisher results, race metadata, BAA qualification standards by age and gender bracket)

## Methods

- Filtered and joined three datasets, keeping 530 of 762 race events flagged as valid qualifying races
- Removed 10,474 invalid records (finish times under 2 hours, including times recorded as 0, and ages under 16, including missing ages coded as 0) and fixed an age-bracket label mismatch that had excluded runners 80+
- Calculated yearly qualification rates and median finish times by gender and age group from runner-level data using dplyr
- Identified top qualifying races among races with 500+ finishers
- Fit models on a 200,000-runner sample stratified by year and qualification status, with an 80/20 train/test split
- Fit three logistic regression models (age, gender, year) with model comparison via AIC and likelihood-ratio tests
- Fit a mixed effects logistic regression with a random intercept for race using lme4, tested with a likelihood-ratio test
- Tested an age × gender interaction term and visualized predicted qualification probabilities
- Evaluated the interaction model on a held-out test set with confusion matrix, precision, recall, F1, and ROC/AUC
- Visualized results using ggplot2 and knitted to PDF via R Markdown

## Models

| # | Model | Features |
|---|-------|----------|
| 1 | Logistic Regression | Age + Gender |
| 2 | Logistic Regression | Age + Age² + Gender |
| 3 | Logistic Regression | Age + Age² + Gender + Year |
| 4 | Interaction Model | Age × Gender + Age² + Year |
| ME | Mixed Effects Logistic Regression | Age + Age² + Gender + Year + (1 \| Race) |

## Results

| Metric | Value |
|--------|-------|
| Overall Qualification Rate | 13.6% |
| Qualification Rate 2022 / 2023 / 2024 | 11.7% / 14.4% / 14.2% |
| Median Finish Time Drop (2022–2024) | 7 minutes |
| Final Model AUC (held-out test set) | 0.562 |
| Race Random Intercept Variance | 0.92 |
| Age × Gender Interaction | OR 0.997 per year, p = 0.005 |

- Qualification rates rose from 11.7% in 2022 to 14.4% in 2023 and held roughly steady in 2024, while median finish times fell 7 minutes over the period
- The 2023 jump in total finishers reflects more races in the dataset (260 vs. 111 in 2022), not higher turnout per race
- Older runners qualify at higher rates, consistent with more lenient age-graded BAA standards, though self-selection among older marathoners may also contribute
- The age × gender interaction was statistically significant but small: the age effect is slightly weaker for men
- Race-level variation is substantial. After accounting for race, the Age² term and the gender effect lose significance and the year effects shrink (2024 odds ratio falls from 1.27 to 1.10), suggesting part of these patterns reflects which runners enter which races
- The top qualifying race among events with 500+ finishers was the AbbottWMM Wanda Age Group World Championship (86%)
- About 80% of non-qualifiers missed their standard by more than 30 minutes; only about 3% came within 5 minutes

## Visuals
Rmd Knit: [Marathon Qualification Analysis](marathon_qualification_analysis.pdf)
