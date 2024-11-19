import yfinance as yf

def download_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.reset_index(inplace=True)  
    stock_data.to_csv(f"data/{ticker}_data.csv", index=False) 
    return stock_data
