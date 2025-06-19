from src.data_loader import get_price_data
from src.cointegration import engle_granger_test
from src.signal_generator import calculate_spread, calculate_zscore, generate_signals
from src.backtester import backtest
from src.performance import calculate_performance
from src.visualization import plot_spread_and_zscore, plot_cumulative_returns

# Two tickers to analyze
ticker1 = "IWM"
ticker2 = "MS"

start_date = "2022-01-01"
end_date = "2024-01-01"

series1 = get_price_data(ticker1, start_date, end_date)
series2 = get_price_data(ticker2, start_date, end_date)

coint_result = engle_granger_test(series1, series2)
print(f"Cointegration Test Result: {coint_result}")

if coint_result['is_cointegrated']:
    spread = calculate_spread(series1, series2, coint_result['beta'])
    zscore = calculate_zscore(spread)
    signals = generate_signals(zscore, entry_threshold=1.0, exit_threshold=0.25)
    results = backtest(series1, series2, coint_result['beta'], signals)
    performance = calculate_performance(results)

    print("\nPerformance Metrics:")
    for key, value in performance.items():
        print(f"{key}: {value:.4f}")

    plot_spread_and_zscore(spread, zscore)
    plot_cumulative_returns(results)
else:
    print("No cointegration found.")
