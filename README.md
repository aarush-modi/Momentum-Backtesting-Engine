# Momentum-Backtesting-Engine

📈 Momentum Strategy Backtester
A fully functional backtesting engine built in Python that:

- Fetches stock data
- Generates momentum-based trading signals
- Simulates portfolio returns
- Calculates risk-adjusted performance metrics
- Visualizes results

💡 Ideal as a first quant-style project combining Python, pandas, SQLite, Matplotlib, and finance.

📦 Features
✅ Fetch historical stock prices (via yfinance)
✅ Simple momentum trading logic
✅ Full portfolio simulation
✅ Sharpe Ratio, Drawdown, Cumulative Return
✅ Interactive equity curve and buy signals plot
✅ Modular design for future strategies

🧠 Strategy Logic
This is a basic momentum strategy:

Buy when today's close is higher than the close N (5) days ago.
Hold until the condition fails.

This can be replaced with any signal in strategies.py.
