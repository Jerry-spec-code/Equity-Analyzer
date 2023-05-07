from re import S
from tkinter import E
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import queries as q 
import util as util

def load_from_yfinance(ticker, start_date, end_date): #Downloads stock data and outputs it to a text file. 
    stock_df = yf.download(ticker, 
                            start = start_date, 
                            end = end_date, 
                            progress = False) #Downloads stocks and saves it in the corresponding dataframe.
    return stock_df.to_string(header = True, index = True)

def get_prices_from_data_frame(data_frame):
    util.write_to_txt(util.PRICES_TXT, data_frame) #Writes the dataframe to the prices.txt file. 
    return util.read_daily_prices(util.PRICES_TXT) #Reads daily price data from prices.txt. 

def update_database_with_price_data(ticker, start_date, end_date, lst):
    q.delete_PDC(ticker, start_date, end_date) #Deletes data between specified start and end date.
    q.insert_ticker(ticker) #insert the ticker into the ticker table. 
    q.insert_PDC(ticker, lst) #inserts data into pridedailyclose table.
    q.insert_search_history(ticker, start_date, end_date)  

def interpret_prices_from_database(database_result):
    headers = ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume']
    util.write_to_csv(util.PRICES_CSV, headers, database_result) #writes the result to a csv file.
    data = pd.read_csv(util.PRICES_CSV) 
    return [
        util.column_to_list(data.date),
        util.column_to_list(data.open),
        util.column_to_list(data.high),
        util.column_to_list(data.low),
        util.column_to_list(data.close),
        util.column_to_list(data.adjclose),
        util.column_to_list(data.volume)
    ]

def get_daily_price_data(ticker, start_date, end_date):
    if q.queried_before(ticker, start_date, end_date): # Checks if price data between specified start and end date already exists in the database.
        data_frame = load_from_yfinance(ticker, start_date, end_date) #Loads data using pyfinance.
        lst = get_prices_from_data_frame(data_frame)
        update_database_with_price_data(ticker, start_date, end_date, lst)
    result = q.get_pdc_data(ticker, start_date, end_date) #gets data from pricedailyclose table.
    return interpret_prices_from_database(result)



