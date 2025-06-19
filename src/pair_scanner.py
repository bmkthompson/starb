import itertools
from src.data_loader import get_price_data
from src.cointegration import engle_granger_test
from src.signal_generator import generate_signals_rolling_beta
from src.backtester import backtest
from src.performance import calculate_performance

def scan_pairs(tickers, start_date, end_date):
    results = []

    data = {ticker: get_price_data(ticker, start_date, end_date) for ticker in tickers}
    pairs = list(itertools.combinations(tickers, 2))

    for ticker1, ticker2 in pairs:
        series1 = data[ticker1]
        series2 = data[ticker2]

        coint_result = engle_granger_test(series1, series2)

        if coint_result['is_cointegrated']:
            signals, spread, zscore, betas = generate_signals_rolling_beta(series1, series2)
            backtest_results = backtest(series1, series2, betas, signals)
            performance = calculate_performance(backtest_results)

            results.append({
                'Pair': f"{ticker1}-{ticker2}",
                'Beta': coint_result['beta'],
                **performance
            })

    return results
