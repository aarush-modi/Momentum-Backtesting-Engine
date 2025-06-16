import pandas as pd

# Generate buy signals using a momentum strategy.
def momentum_strategy (data: pd.DataFrame, lookback: int = 5) -> pd.DataFrame:
    df = data.copy()
    df['Signal'] = 0
    df['Signal'] = (df['Close'] > df['Close'].shift(lookback)).astype(int)
    df['Signal'] = df['Signal'].shift(1)
    df.dropna(inplace=True)
    return df
