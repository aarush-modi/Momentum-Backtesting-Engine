import matplotlib.pyplot as plt
import pandas as pd

# Portfolio equity over time
def plot_equity_curve(df: pd.DataFrame, title: str = "Equity Curve"):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Equity'], label='Equity Curve', color='blue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value ($)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Stock prices and buy signals
def plot_signals(df: pd.DataFrame, title: str = "Buy Signals on Price"):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Price', color='black')

    # Buy markers
    buy_signals = df[df['Signal'] == 1]
    plt.plot(buy_signals.index, buy_signals['Close'], '^', color='green', markersize=10, label='Buy')

    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
