import pandas as pd

def calculate_spread(series1, series2, beta):
    df = pd.concat([series1, series2], axis=1).dropna()
    spread = df.iloc[:, 0] - beta * df.iloc[:, 1]
    return spread

def calculate_zscore(spread, window=30):
    mean = spread.rolling(window).mean()
    std = spread.rolling(window).std()
    zscore = (spread - mean) / std
    return zscore

def generate_signals(zscore, entry_threshold=1.0, exit_threshold=0.25):
    signals = pd.Series(index=zscore.index, dtype='float64')
    
    signals[zscore > entry_threshold] = -1  # Short spread
    signals[zscore < -entry_threshold] = 1  # Long spread
    signals[abs(zscore) < exit_threshold] = 0  # Exit position

    signals.ffill(inplace=True)
    return signals
