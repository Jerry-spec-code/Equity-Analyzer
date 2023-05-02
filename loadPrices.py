from re import S
from tkinter import E
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import queries as q 
import csv

pricesTXT = 'txtPrices.txt'
pricesCSV = 'csvPrices.csv'

def load(ticker, startDate, endDate): #Downloads stock data and outputs it to a text file. 
    stock_df = yf.download(ticker, 
                            start = startDate, 
                            end = endDate, 
                            progress = False) #Downloads stocks and saves it in the corresponding dataframe.
    write_to_txt(pricesTXT, stock_df.to_string(header = True, index = True)) #Writes the dataframe to the prices.txt file. 

def write_to_txt(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)

def write_to_csv(header, body): #Writes the data to the 'prices.csv' file. 
    with open(pricesCSV, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)

def readDailyPrices(lst): #Reads the data from prices.txt 
    with open(pricesTXT) as file:
        for i, line in enumerate(file):
            if i < 2: 
                continue
            else:
                temp = []
                for word in line.split():
                    temp.append(word)
                lst.append(temp)

def column_to_list(data):
    return [row for row in data]

def getPriceData(ticker, startDate, endDate):
    if q.new_search(ticker, startDate, endDate): # Checks if price data between specified start and end date already exists in the database.
        q.deleteFromPDC(ticker, startDate, endDate) #Deletes data between specified start and end date.
        load(ticker, startDate, endDate) #Loads data using pyfinance.
        q.insertIntoTicker(ticker) #insert the ticker into the ticker table. 
        lst = []
        readDailyPrices(lst) #Reads daily price data from prices.txt. 
        q.insertIntoPDC(ticker, lst) #inserts data into pridedailyclose table.
        result = q.getPDCData(ticker, startDate, endDate) #gets data from pricedailyclose table.
        q.insertIntoSearchHistory(ticker, startDate, endDate) 
    else:
        result = q.getPDCData(ticker, startDate, endDate) #gets data from pricedailyclose table.
    header = ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume']
    write_to_csv(header, result) #writes the result to a csv file.
    data = pd.read_csv(pricesCSV) 
    return [
        column_to_list(data.date),
        column_to_list(data.open),
        column_to_list(data.high),
        column_to_list(data.low),
        column_to_list(data.close),
        column_to_list(data.adjclose),
        column_to_list(data.volume)
    ]


