import mysql.connector

from serverInfo import host
from serverInfo import database
from serverInfo import user
from serverInfo import password

def modifyList(tickerid, PDClst): #Price daily close lst
    PDClst.insert(0, tickerid)

def deleteFromPDC(my_ticker, start, end): #Deletes data between specified start and end date.
    try: 
        connection = mysql.connector.connect(host = host, 
        database = database, user = user, password = password)
        sql_delete_Query = "DELETE p FROM pricedailyclose p inner join ticker t on t.tickerid = p.tickerid AND t.ticker = (%s) where p.date between (%s) and (%s)"
        cursor = connection.cursor()
        cursor.execute(sql_delete_Query, (my_ticker, start, end))
        connection.commit()
    
    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()

def insertIntoPDC(my_ticker, lst): ##inserts data into price daily close table 
    try: 
        connection = mysql.connector.connect(host = host, 
        database = database, user = user, password = password)
        cursor = connection.cursor()
        sql_tickerID_Query = "select tickerid from ticker where ticker = (%s)"
        cursor.execute(sql_tickerID_Query, (my_ticker, ))
        records = cursor.fetchall()
        ticker_id = records[0][0]

        for i in lst:
            modifyList(ticker_id, i)
            tpl = tuple(i)
            sql_insert_Query = "insert into pricedailyclose (tickerid, date, open, high, low, close, adjclose, volume) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_insert_Query, tpl)
            connection.commit()

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("Data inserted into pricedailyclose table")

def deleteFromTicker(my_ticker): #Deletes data from ticker table based on specified ticker. 
    try: 
        connection = mysql.connector.connect(host = host, 
        database = database, user = user, password = password)
        sql_delete_Query = "DELETE FROM ticker where ticker = %s"
        cursor = connection.cursor()
        cursor.execute(sql_delete_Query, (my_ticker, ))
        connection.commit()
    
    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("Data deleted from ticker table")

def insertIntoTicker(my_ticker): #Inserts data from ticker table based on specified ticker. 
    try: 
        connection = mysql.connector.connect(host = host, 
        database = database, user = user, password = password)
        sql_insertIntoTicker_Query = "insert into ticker (ticker) select (%s) where not exists (select ticker from ticker where ticker = (%s)) limit 1;"
        cursor = connection.cursor() 
        cursor.execute(sql_insertIntoTicker_Query, (my_ticker, my_ticker))
        connection.commit()
    
    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("Date inserted into ticker table")

def getPDCData(my_ticker, startDate, endDate): #Gets data from pricedailyclose table. 
    try: 
        connection = mysql.connector.connect(host = host, 
        database = database, user = user, password = password)
        cursor = connection.cursor()
        sql_select_Query = ("select date, open, high, low, close, adjclose, volume from pricedailyclose p" 
                            " inner join ticker t on t.tickerid = p.tickerid" 
                            " AND t.ticker = (%s) where p.date between (%s) and (%s)")
        cursor.execute(sql_select_Query, (my_ticker, startDate, endDate))
        records = cursor.fetchall()

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("Data retrieved from price daily close table")
            return records

def insertIntoSearchHistory(my_ticker, startDate, endDate):
    try: 
        connection = mysql.connector.connect(host = host, 
        database = database, user = user, password = password)
        cursor = connection.cursor()
        sql_insert_Query = "insert into searchhistory (ticker, startdate, enddate) values (%s, %s, %s)"
        cursor.execute(sql_insert_Query, (my_ticker, startDate, endDate))
        connection.commit()

    except mysql.connector.Error as e:
        print("Error reading data: " , e)
    
    finally:
        if connection.is_connected(): 
            connection.close()
            cursor.close()
            print("Data inserted into search history table")

# Checks if price data between specified start and end date already exists.
def new_search(my_ticker, startDate, endDate):
    try: 
        connection = mysql.connector.connect(host = host, 
        database = database, user = user, password = password)
        cursor = connection.cursor()
        sql_select_Query = "select count(*) from searchhistory where ticker = (%s) and startdate <= (%s) and enddate >= (%s)"
        cursor.execute(sql_select_Query, (my_ticker, startDate, endDate))
        records = cursor.fetchall()
    
    except mysql.connector.Error as e:
        print("Error reading data: " , e)
    
    finally:
        if connection.is_connected(): 
            connection.close()
            cursor.close()
            print("Data read from search history table")
            return records[0][0] == 0
