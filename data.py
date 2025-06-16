import yfinance as yf
import pandas as pd


# Download historical stock data usihng yfinance
def get_data (ticker: str, start: str, end: str, auto_adjust = False) -> pd.DataFrame:
    df = yf.download(ticker, start = start, end = end)
    if df.empty:
        raise ValueError ("No data found. Check Ticker: " + ticker)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace = True)
    return df