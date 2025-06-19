import numpy as np

def calculate_performance(results, risk_free_rate=0.0):
    trading_days = 252

    total_return = results['Cumulative_ret'].iloc[-1] - 1
    annual_return = (results['Cumulative_ret'].iloc[-1]) ** (trading_days / len(results)) - 1
    annual_volatility = results['Strategy_ret'].std() * np.sqrt(trading_days)

    if annual_volatility != 0:
        sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility
    else:
        sharpe_ratio = np.nan

    cumulative = results['Cumulative_ret']
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()

    win_rate = (results['Strategy_ret'] > 0).sum() / (results['Strategy_ret'].count())

    return {
        'Total Return': total_return,
        'Annualized Return': annual_return,
        'Annualized Volatility': annual_volatility,
        'Sharpe Ratio': sharpe_ratio,
        'Max Drawdown': max_drawdown,
        'Win Rate': win_rate
    }
