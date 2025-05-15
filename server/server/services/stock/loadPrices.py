import server.models.stock.queries as q 
from server.services.marketData.loadPrices import load_from_yfinance
import pandas as pd
from datetime import datetime

def column_to_list(column, cast=lambda x : x):
    return [cast(data) for data in column]

def get_prices_from_data_frame(data_frame):
    if 'Empty DataFrame' in data_frame:
        return []
    return [row.split() for row in data_frame.splitlines()][3:]

def update_database_with_price_data(ticker, start_date, end_date, lst):
    q.delete_PDC(ticker, start_date, end_date) #Deletes data between specified start and end date.
    q.insert_ticker(ticker) #insert the ticker into the ticker table. 
    q.insert_PDC(ticker, lst) #inserts data into pridedailyclose table.
    q.insert_search_history(ticker, start_date, end_date)  

def interpret_prices_from_database(database_result):
    headers = ['date', 'close', 'high', 'low', 'open', 'volume']
    data = pd.DataFrame(database_result, columns=headers)
    date_cast = lambda date : datetime.strftime(date, '%Y-%m-%d')
    return [
        column_to_list(data.date, cast=date_cast),
        column_to_list(data.open, cast=float),
        column_to_list(data.high, cast=float),
        column_to_list(data.low, cast=float),
        column_to_list(data.close, cast=float),
        column_to_list(data.volume, cast=float),
    ]

def get_daily_price_data(input_object):
    ticker, start_date, end_date = input_object['ticker'], input_object['start_date'], input_object['end_date']
    if q.not_queried_before(ticker, start_date, end_date): # Checks if price data between specified start and end date already exists in the database.
        data_frame = load_from_yfinance(ticker, start_date, end_date) #Loads data using pyfinance.
        lst = get_prices_from_data_frame(data_frame)
        update_database_with_price_data(ticker, start_date, end_date, lst)
    result = q.get_pdc_data(ticker, start_date, end_date) #gets data from pricedailyclose table.
    return interpret_prices_from_database(result)
