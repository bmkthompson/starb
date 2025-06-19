import matplotlib.pyplot as plt

def plot_spread_and_zscore(spread, zscore, entry_threshold=1.0, exit_threshold=0.25):
    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.plot(spread.index, spread, label='Spread', color='blue')
    ax1.set_ylabel('Spread')
    ax1.legend(loc='upper left')

    ax2 = ax1.twinx()
    ax2.plot(zscore.index, zscore, label='Z-Score', color='red')
    ax2.axhline(entry_threshold, color='green', linestyle='--')
    ax2.axhline(-entry_threshold, color='green', linestyle='--')
    ax2.axhline(exit_threshold, color='orange', linestyle=':')
    ax2.axhline(-exit_threshold, color='orange', linestyle=':')
    ax2.set_ylabel('Z-Score')
    ax2.legend(loc='upper right')

    plt.title("Spread & Z-Score")
    plt.show()

def plot_cumulative_returns(results):
    plt.figure(figsize=(12,6))
    plt.plot(results.index, results['Cumulative_ret'], label='Cumulative Return')
    plt.title("Backtest Cumulative Return")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.show()
