import numpy as np
import pandas as pd
import statsmodels.api as sm

def calculate_rolling_beta(series1, series2, window):
    betas = []
    for i in range(len(series1)):
        if i < window:
            betas.append(np.nan)
            continue
        y_window = series1.iloc[i-window:i]
        x_window = series2.iloc[i-window:i]
        x_with_const = sm.add_constant(x_window)
        model = sm.OLS(y_window, x_with_const).fit()
        beta = model.params[1]
        betas.append(beta)
    return pd.Series(betas, index=series1.index)

def generate_signals_rolling_beta(series1, series2, window=60, z_entry=1.0, z_exit=0.5):
    betas = calculate_rolling_beta(series1, series2, window)
    spread = series1 - betas * series2

    spread_mean = spread.rolling(window).mean()
    spread_std = spread.rolling(window).std()
    zscore = (spread - spread_mean) / spread_std

    signals = pd.Series(0, index=series1.index)
    signals[zscore > z_entry] = -1
    signals[zscore < -z_entry] = 1
    signals[(zscore < z_exit) & (zscore > -z_exit)] = 0

    return signals, spread, zscore, betas
