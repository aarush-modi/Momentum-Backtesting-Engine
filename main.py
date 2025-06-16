from data import get_data
from strategies import momentum_strategy
from backtest import run_backtest
from metrics import cumulative_return, max_drawdown, sharpe_ratio
from plot import plot_equity_curve, plot_signals

def main():
    print("📊 Momentum Strategy Backtester")

    ticker = input("Enter stock ticker (e.g. AAPL): ").upper()
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")

    try:
        # Step 1: Load Data
        df = get_data(ticker, start, end)

        # Step 2: Apply Strategy
        df = momentum_strategy(df, lookback=5)

        # Step 3: Run Backtest
        results = run_backtest(df)

        # Step 4: Show Metrics
        print("\n📈 Performance Metrics:")
        print(f"Cumulative Return: {cumulative_return(results)}%")
        print(f"Max Drawdown: {max_drawdown(results)}%")
        print(f"Sharpe Ratio: {sharpe_ratio(results)}")

        # Step 5: Plot
        plot_equity_curve(results, title=f"{ticker} - Equity Curve")
        plot_signals(results, title=f"{ticker} - Buy Signals")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
