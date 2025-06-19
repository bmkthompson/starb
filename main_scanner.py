import pandas as pd
from src.pair_scanner import scan_pairs

# Full universe to scan
tickers = [
    "SPY", "QQQ", "DIA", "IWM", "VTI", "VOO", 
    "AAPL", "MSFT", "GOOG", "META", "AMZN", "NVDA", "TSLA",
    "JPM", "BAC", "GS", "MS",
    "XOM", "CVX", "COP",
    "UNH", "JNJ", "PFE", 
    "WMT", "COST", "HD", "TGT",
    "DIS", "NFLX", "PEP", "KO"
]

start_date = "2022-01-01"
end_date = "2024-01-01"

results = scan_pairs(tickers, start_date, end_date)

if results:
    df = pd.DataFrame(results)
    df = df.sort_values(by='Sharpe Ratio', ascending=False)

    print(f"\n✅ Cointegrated pairs found: {len(df)}\n")
    print(df[['Pair', 'Sharpe Ratio', 'Total Return', 'Max Drawdown', 'Win Rate']].to_string(index=False))

    # Export results to CSV
    df.to_csv("scanner_results.csv", index=False)
    print("\n📄 Results saved to scanner_results.csv")

else:
    print("No cointegrated pairs found.")
