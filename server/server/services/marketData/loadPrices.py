import yfinance as yf

def load_from_yfinance(ticker, start_date, end_date):
    stock_df = yf.download(ticker, 
                            start = start_date, 
                            end = end_date, 
                            progress = False) #Downloads stocks and saves it in the corresponding dataframe.
    return stock_df.to_string(header = True, index = True)
