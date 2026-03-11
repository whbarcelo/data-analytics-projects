# Data Analytics Projects Portfolio
By William Barcelo

This repository contains my data analytics projects using Python, R, and SQL.  
Each project includes code, visualizations, and written analysis interpreting results.

---
## Projects

---
### 1. Economic Indicators and S&P 500 Sector Analysis - SQL + Python
SQL-based analysis exploring the relationship between macroeconomic indicators and S&P 500 sector performance from 2000 to 2025.

Folder: [S&P 500 Sector Analysis](Projects/SQL/S&P%20500%20Sector%20Analysis)

File: [Jupyter Notebook](Projects/SQL/S&P%20500%20Sector%20Analysis/economics_analysis.ipynb)

Highlights:
- Designed a 4-table SQLite database combining FRED macroeconomic data with S&P 500 sector ETF data
- Wrote 6 progressive SQL queries using CTEs, window functions, and multi-table JOINs
- Identified sector rotation patterns across economic cycles (contraction, slow growth, moderate growth, strong growth)
- Found Technology outperformed all sectors during high inflation periods, contradicting conventional thinking
- Determined Energy had the highest raw returns during strong growth but ranked last on a risk-adjusted basis due to extreme volatility
- Visualized results using Matplotlib

---
### 2. Boston Marathon Qualification Analysis – R + ggplot2
Analysis of Boston Marathon qualification trends across 1,081,649 runners from 762 qualifying races between 2022 and 2024.

Folder: [Boston Marathon Qualification Analysis](Projects/R/Boston%20Marathon%20Qualification%20Analysis)

File: [R Markdown](Projects/R/Boston%20Marathon%20Qualification%20Analysis/marathon_qualification_analysis.rmd) | [PDF Report](Projects/R/Boston%20Marathon%20Qualification%20Analysis/marathon_qualification_analysis.pdf)

Highlights:
- Analyzed qualification rates and finish time trends across 532 races by year, gender, and age group
- Identified top qualifying races among events with 500+ finishers; Highwayman Dash exceeded 75% qualification rate
- Found the majority of non-qualifiers missed their standard by 30+ minutes, suggesting the BQ standard is a hard ceiling for most runners
- Fit logistic regression models with AIC/chi-square comparison; added mixed effects model with random intercept for race (variance = 0.96)
- Age × gender interaction was not statistically significant (p = 0.118), suggesting the age effect is consistent across genders
- Final model achieved AUC of 0.569 using only demographic and temporal features, with target leakage avoided by excluding finish time

---
### 3. Student Exam Score Prediction – Python (scikit-learn)
Prediction model using the UCI Student Performance dataset.

Folder: [Student Exam Score Prediction](Projects/Python/Student%20Exam%20Score%20Regression/student_scores_regression.ipynb)

Notebook: [Jupyter Notebook](Projects/Python/student_scores_regression.ipynb)

Highlights:
- Built regression models to predict final exam score ("G3")
- Improved model performance from R² = -0.048 → 0.708
- Used EDA, visualization (heatmaps, scatterplots), and feature engineering
- Identified strongest predictors — previous grades and extra academic support were most important

---
## Tools and Skills
Languages: Python, R, SQL

Libraries: Pandas, NumPy, Scikit-learn, tidyverse, ggplot2, lme4, knitr, Matplotlib, Seaborn, SQLite3

Techniques: Regression modeling, logistic regression, mixed effects models, EDA, feature interpretation, diagnostics, ROC/AUC evaluation, CTEs, window functions, multi-table JOINs, database design

Feel free to explore the project folders above!
