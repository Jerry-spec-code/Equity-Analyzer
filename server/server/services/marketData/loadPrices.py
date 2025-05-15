import yfinance as yf

def load_from_yfinance(ticker, start_date, end_date):
    stock_df = yf.download(ticker, 
                            start = start_date, 
                            end = end_date) #Downloads stocks and saves it in the corresponding dataframe.
    res = stock_df.to_string(header = True, index = True)
    return res
