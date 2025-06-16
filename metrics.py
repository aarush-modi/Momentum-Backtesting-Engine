import pandas as pd
import numpy as np


def cumulative_return(df = pd.DataFrame) -> float:
    return_pct = (df['Equity'].iloc[-1] / df['Equity'].iloc[0]) - 1
    return round(return_pct * 100, 2)

def max_drawdown(df = pd.DataFrame) -> float:
    cumulative_max = df['Equity'].cummax()
    drawdown = df['Equity'] / cumulative_max - 1
    max_dd = drawdown.min()
    return round(max_dd * 100, 2)

def sharpe_ratio(df: pd.DataFrame, risk_free_rate: float = 0.01) -> float:
    excess_returns = df['Daily Return'] - (risk_free_rate / 252)
    mean_excess = excess_returns.mean()
    std_dev = excess_returns.std()
    sharpe = np.sqrt(252) * mean_excess / std_dev if std_dev != 0 else 0
    return round(sharpe, 2)