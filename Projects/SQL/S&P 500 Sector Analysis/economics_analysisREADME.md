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
| 4 | Sector returns by inflation regime (year-over-year CPI) | Chained CTEs, LAG() window function, CASE |
| 5 | Rolling 4-quarter GDP growth vs market returns | Chained CTEs, ROWS BETWEEN window frame |
| 6 | Sector rankings by return/volatility ratio per economic cycle | Three chained CTEs, NULLIF, RANK() |

---

## Results

Cycles are defined by each quarter’s annualized real GDP growth (Contraction < 0%, Slow 0–2%, Moderate 2–4%, Strong > 4%). Risk-adjusted return = average monthly return ÷ range of monthly returns in the quarter.

| Economic Cycle | Top Sector (Risk-Adjusted) | Worst Sector (Risk-Adjusted) |
|----------------|---------------------------|------------------------------|
| Contraction | Consumer Discretionary* | Financials |
| Slow Growth | Healthcare | Energy |
| Moderate Growth | Consumer Discretionary | Consumer Staples |
| Strong Growth | Consumer Staples | Utilities |

- Every sector lost money on average during contractions. Financials fell furthest (−2.91% per month) and ranked last on both raw and risk-adjusted return, consistent with the 2008 financial crisis
- *Consumer Discretionary ranks first in contractions only because of how the ratio behaves with negative returns: dividing a loss by higher volatility moves the ratio toward zero. On raw return, Consumer Staples (−0.77%), Utilities, and Healthcare held up best
- Energy had the highest return volatility in three of the four cycles; during strong growth it had the highest raw return (+2.76% per month) but ranked seventh after adjusting for volatility
- Consumer Staples ranked first during strong growth because it had the lowest volatility, not the highest return (fourth of eight)
- When year-over-year inflation exceeded 3%, Energy had the highest average monthly return (+1.21%) and Financials the lowest (−0.03%); Technology ranked sixth. Energy was the only sector with a meaningfully higher return in high-inflation months than in low-inflation months (+1.21% vs. +0.88%); Utilities was roughly flat. Because energy prices are part of CPI, this relationship runs in both directions

---
