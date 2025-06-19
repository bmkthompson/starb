Cointegration-based Statistical Arbitrage Engine

This project implements a complete statistical arbitrage pipeline using cointegration to identify and trade mean-reverting pairs.

Key Features

- Automatic data ingestion via Yahoo Finance (yfinance)
- Stationarity tests (ADF)
- Engle-Granger cointegration test
- Hedge ratio estimation (OLS regression)
- Z-score based signal generation
- Backtesting engine with realistic trade simulation
- Performance evaluation (Sharpe Ratio, Total Return, Max Drawdown, Win Rate)
- Multi-pair scanner across entire ticker universes
- Clean visualization for single pair analysis
- CSV export of backtest results

Technologies

- Python
- pandas
- numpy
- statsmodels
- matplotlib
- yfinance

How It Works

1️⃣ You define a universe of tickers.  
2️⃣ The system tests all pairwise combinations for cointegration.  
3️⃣ Cointegrated pairs are backtested with trading signals based on z-score of the spread.  
4️⃣ Performance metrics are calculated and exported.

Files

- `main_scanner.py` → full multi-pair scanner
- `main_single.py` → deep analysis of a specific pair with full visuals
- `src/` → modular codebase containing full engine logic


Example Results

See `scanner_results.csv` for example backtest results.


Example Output (top cointegrated pairs)

| Pair | Sharpe Ratio | Total Return | Max Drawdown | Win Rate |
|------|--------------|--------------|--------------|----------|
| UNH-KO | 1.66 | 66.6% | -12% | 41% |
| GS-HD | 1.56 | 61.9% | -13% | 39% |
| ... | ... | ... | ... | ... |

Next Development Steps

- Rolling-window cointegration stability ✅ (implemented 06-2025)
- Transaction cost simulation
- Portfolio allocation logic
- Live trading capability

---

**Built as a personal quant research project to demonstrate professional quant development workflow.**
