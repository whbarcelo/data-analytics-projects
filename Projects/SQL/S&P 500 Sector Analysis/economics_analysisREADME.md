# Economic Indicators & S&P 500 Sector Analysis - SQL + Python
Goal: Analyze the relationship between macroeconomic indicators and S&P 500 sector performance across economic cycles from 2000 to 2025.  
Dataset: FRED (CPI, GDP, Unemployment, Federal Funds Rate) + Yahoo Finance S&P 500 Sector ETFs (XLK, XLF, XLE, XLV, XLY, XLP, XLI, XLU)

---

## Methods
- Designed a 4-table SQLite database (macro_indicators, sp500_sectors, companies, recessions)
- Loaded and merged macroeconomic CSV data from FRED using Pandas
- Calculated monthly sector returns (pct_change) using Pandas and stored results in SQLite
- Wrote 6 progressive SQL queries using CTEs, window functions, and multi-table JOINs
- Visualized results using Matplotlib

---

## Queries
| # | Query | SQL Features Used |
|---|-------|------------------|
| 1 | Average sector returns by year | GROUP BY, aggregations, strftime |
| 2 | Top companies by market cap per sector | RANK(), PARTITION BY, window functions |
| 3 | Macro data joined with sector performance by quarter | JOIN, CASE, quarterly aggregation |
| 4 | Sectors by CPI regime | CTE, subquery, CASE |
| 5 | Rolling 4-quarter GDP growth vs market returns | Chained CTEs, ROWS BETWEEN window frame |
| 6 | Sector rankings by return/volatility ratio per economic cycle | Three chained CTEs, NULLIF, RANK() |

---

## Results

Cycles are defined by each quarter’s annualized real GDP growth (Contraction < 0%, Slow 0–2%, Moderate 2–4%, Strong > 4%). Risk-adjusted return = average monthly return ÷ range of monthly returns in the quarter.

| Economic Cycle | Top Sector (Risk-Adjusted) | Worst Sector (Risk-Adjusted) |
|----------------|---------------------------|------------------------------|
| Contraction | Consumer Staples | Technology |
| Slow Growth | Healthcare | Energy |
| Moderate Growth | Industrials | Energy |
| Strong Growth | Technology | Utilities |

- Every sector posted a negative average return during contractions; Consumer Staples and Healthcare ranked first and second on a risk-adjusted basis
- Technology had the most cyclical profile (first on a risk-adjusted basis during strong growth and last during contractions)
- Energy had the highest return volatility in three of the four cycles and ranked last on a risk-adjusted basis during slow and moderate growth
- Technology had the highest average return when CPI was more than 10% above its 2000–2025 average (roughly late 2020 onward)

---

## Visuals
Average Monthly Return by Sector and Year: [Sector Returns by Year](economics_analysis_plots/AverageMonthlyReturnbySectorandYear.jpg)

Technology Returns vs CPI: [Tech Returns vs CPI](economics_analysis_plots/TechnologySectorReturnsvsCPIbyQuarter.jpg)

Energy Returns vs Rolling GDP: [Energy Returns vs GDP](economics_analysis_plots/EnergySectorReturnsvsRollingGDPGrowth.jpg)

Sector Risk-Adjusted Returns by Economic Cycle: [Risk-Adjusted Returns](economics_analysis_plots/SectorRisk-AdjustedReturnsbyEconomicCycle.jpg)
