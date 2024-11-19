import pandas as pd
import matplotlib.pyplot as plt

def create_graph(input_file):
    data = pd.read_csv(input_file, index_col="Date", parse_dates=True)

    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['Short_MA'], label='20-Day MA', linestyle='--', color='orange')
    plt.plot(data['Long_MA'], label='50-Day MA', linestyle='--', color='green')

    plt.title("Apple Stock Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.savefig("outputs/apple_stock_moving_averages.png")
    plt.show()
