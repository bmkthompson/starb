from statsmodels.tsa.stattools import adfuller

def adf_test(series, significance=0.05):
    series = series.squeeze()
    result = adfuller(series.dropna())
    test_stat = result[0]
    p_value = result[1]
    is_stationary = p_value < significance

    return {
        'ADF Statistic': test_stat,
        'p-value': p_value,
        'is_stationary': is_stationary
    }
