import server.models.stock.queries as q 
from server.services.marketData.loadPrices import load_from_yfinance
import csv
import pandas as pd

PRICES_TXT = 'txtPrices.txt'
PRICES_CSV = 'csvPrices.csv'

def write_to_txt(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)

def write_to_csv(filename, header, body):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)

def read_daily_prices(filename):
    lst = []
    with open(filename) as file:
        for i, line in enumerate(file):
            if i < 2: 
                continue
            else:
                temp = []
                for word in line.split():
                    temp.append(word)
                lst.append(temp)
    return lst

def column_to_list(data):
    return [row for row in data]

def get_prices_from_data_frame(data_frame):
    write_to_txt(PRICES_TXT, data_frame) #Writes the dataframe to the prices.txt file. 
    return read_daily_prices(PRICES_TXT) #Reads daily price data from prices.txt. 

def update_database_with_price_data(ticker, start_date, end_date, lst):
    q.delete_PDC(ticker, start_date, end_date) #Deletes data between specified start and end date.
    q.insert_ticker(ticker) #insert the ticker into the ticker table. 
    q.insert_PDC(ticker, lst) #inserts data into pridedailyclose table.
    q.insert_search_history(ticker, start_date, end_date)  

def interpret_prices_from_database(database_result):
    headers = ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume']
    write_to_csv(PRICES_CSV, headers, database_result) #writes the result to a csv file.
    data = pd.read_csv(PRICES_CSV) 
    return [
        column_to_list(data.date),
        column_to_list(data.open),
        column_to_list(data.high),
        column_to_list(data.low),
        column_to_list(data.close),
        column_to_list(data.adjclose),
        column_to_list(data.volume)
    ]

def get_daily_price_data(input_object):
    ticker, start_date, end_date = input_object['ticker'], input_object['start_date'], input_object['end_date']
    if q.not_queried_before(ticker, start_date, end_date): # Checks if price data between specified start and end date already exists in the database.
        data_frame = load_from_yfinance(ticker, start_date, end_date) #Loads data using pyfinance.
        lst = get_prices_from_data_frame(data_frame)
        update_database_with_price_data(ticker, start_date, end_date, lst)
    result = q.get_pdc_data(ticker, start_date, end_date) #gets data from pricedailyclose table.
    return interpret_prices_from_database(result)
