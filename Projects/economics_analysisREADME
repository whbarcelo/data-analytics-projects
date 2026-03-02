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
| 4 | Sectors that outperform during high inflation | CTE, subquery, CASE |
| 5 | Rolling 4-quarter GDP growth vs market returns | Chained CTEs, ROWS BETWEEN window frame |
| 6 | Sector rankings by return/volatility ratio per economic cycle | Three chained CTEs, NULLIF, RANK() |

---

## Results
| Economic Cycle | Top Sector (Risk-Adjusted) | Worst Sector (Risk-Adjusted) |
|----------------|---------------------------|------------------------------|
| Contraction | Consumer Discretionary | Financials |
| Slow Growth | Healthcare | Energy |
| Moderate Growth | Consumer Discretionary | Financials |
| Strong Growth | Consumer Staples | Utilities |

- Technology outperformed all sectors during high inflation periods, contradicting conventional wisdom
- Energy had the highest raw returns during strong growth (+0.70%) but ranked last on a risk-adjusted basis due to extreme volatility
- Financials were hit hardest during contractions, consistent with the 2008 financial crisis
- Consumer Staples delivered the best risk-adjusted returns during strong economic growth

---

## Visuals
Average Monthly Return by Sector and Year: [Sector Returns by Year](economics_analysis_plots/AverageMonthlyReturnbySectorandYear.jpg)
Technology Returns vs CPI: [Tech Returns vs CPI](economics_analysis_plots/TechnologySectorReturnsvsCPIbyQuarter.jpg)
Energy Returns vs Rolling GDP: [Energy Returns vs GDP](economics_analysis_plots/EnergySectorReturnsvsRollingGDPGrowth.jpg)
Sector Risk-Adjusted Returns by Economic Cycle: [Risk-Adjusted Returns](economics_analysis_plots/SectorRisk-AdjustedReturnsbyEconomicCycle.jpg)
