import pandas as pd


# Backtest a signal-based strategy. Buys when 'Signal' == 1.
def run_backtest (data: pd.DataFrame, initial_cash: float = 10000) -> pd.DataFrame:
    df = data.copy()
    df['Position'] = 0
    df['Cash'] = initial_cash
    df['Holdings'] = 0
    df['Equity'] = initial_cash
    df['Daily Return'] = 0.0

    position = 0
    cash = initial_cash

    for i in range (1, len(df)):
        signal = df['Signal'].iloc[i]

        if signal == 1 and position == 0:
            price = df['Close'].iloc[i]
            position = cash / price  # Buy max shares
            cash = 0
        
        elif signal == 0 and position > 0:
            price = df['Close'].iloc[i]
            cash = position * price
            position = 0

        price = df['Close'].iloc[i]
        holdings = position * price
        equity = cash + holdings
        prev_equity = df['Equity'].iloc[i - 1]

        df.at[df.index[i], 'Position'] = position
        df.at[df.index[i], 'Cash'] = cash
        df.at[df.index[i], 'Equity'] = equity
        df.at[df.index[i], 'Daily Return'] = (equity - prev_equity)/prev_equity
    
    return df
