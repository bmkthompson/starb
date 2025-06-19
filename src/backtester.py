import pandas as pd

def backtest(series1, series2, beta, signals):
    df = pd.concat([series1, series2, signals], axis=1).dropna()
    df.columns = ['A', 'B', 'Signal']

    if isinstance(beta, pd.Series):
        beta = beta.reindex(df.index).fillna(method='ffill')
        df['Beta'] = beta
    else:
        df['Beta'] = beta

    df['A_ret'] = df['A'].pct_change()
    df['B_ret'] = df['B'].pct_change()

    df['Strategy_ret'] = df['Signal'].shift(1) * (df['A_ret'] - df['Beta'] * df['B_ret'])
    df['Cumulative_ret'] = (1 + df['Strategy_ret']).cumprod()

    return df[['Strategy_ret', 'Cumulative_ret']]
