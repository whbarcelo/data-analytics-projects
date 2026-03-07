# Data Analytics Projects Portfolio
By William Barcelo

This repository contains my data analytics projects using Python, R, and SQL.  
Each project includes code, visualizations, and written analysis interpreting results.

---
## Projects

### 1. Student Exam Score Prediction – Python (scikit-learn)
Prediction model using the UCI Student Performance dataset.

Folder: [Project Folder](Projects/)

Notebook: [Jupyter Notebook](Projects/student_scores_regression.ipynb)

Highlights:
- Built regression models to predict final exam score ("G3")
- Improved model performance from R² = -0.048 → 0.708
- Used EDA, visualization (heatmaps, scatterplots), and feature engineering
- Identified strongest predictors — previous grades and extra academic support were most important

---
### 2. Fuel Efficiency Regression Analysis – R
Statistical modeling using the 'mtcars' dataset.

Folder: [Project Folder](Projects/)

File: [R Markdown](Projects/fuel_efficiency_analysis.Rmd)

Highlights:
- Ran EDA to study relationship between mpg & vehicle traits
- Built simple vs multiple regression models; Adjusted R² improved
- Compared models with ANOVA and evaluated diagnostic plots
- Interpreted coefficients and visualized predictor influence

---
### 3. Economic Indicators and S&P 500 Sector Analysis - SQL + Python
SQL-based analysis exploring the relationship between macroeconomic indicators and S&P 500 sector performance from 2000 to 2025.

Folder: [Project Folder](Projects/)

File: [Jupyter Notebook](Projects/economics_analysis.ipynb)

Highlights:
- Designed a 4-table SQLite database combining FRED macroeconomic data with S&P 500 sector ETF data
- Wrote 6 progressive SQL queries using CTEs, window functions, and multi-table JOINs
- Identified sector rotation patterns across economic cycles (contraction, slow growth, moderate growth, strong growth)
- Found Technology outperformed all sectors during high inflation periods, contradicting conventional thinking
- Determined Energy had the highest raw returns during strong growth but ranked last on a risk-adjusted basis due to extreme volatility
- Visualized results using Matplotlib

---

## Tools and Skills
Languages: Python, R, SQL

Libraries: Pandas, NumPy, Scikit-learn, tidyverse, ggplot2, Matplotlib, Seaborn, SQLite3

Techniques: Regression modeling, EDA, feature interpretation, diagnostics, ANOVA, CTEs, window functions, multi-table JOINs, database design

Feel free to explore the project folders above!
