from connection import getConnection, closeConnectionAndCursor

def deleteFromPDC(my_ticker, start, end): #Deletes data between specified start and end date.
    try: 
        connection = getConnection()
        sql_delete_Query = "DELETE p FROM pricedailyclose p inner join ticker t on t.tickerid = p.tickerid AND t.ticker = (%s) where p.date between (%s) and (%s)"
        cursor = connection.cursor()
        cursor.execute(sql_delete_Query, (my_ticker, start, end))
        connection.commit()
    
    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Data deleted from price daily close table"
        closeConnectionAndCursor(connection, cursor, message)

def insertIntoPDC(my_ticker, lst): ##inserts data into price daily close table 
    try: 
        connection = getConnection()
        cursor = connection.cursor()
        sql_tickerID_Query = "select tickerid from ticker where ticker = (%s)"
        cursor.execute(sql_tickerID_Query, (my_ticker, ))
        records = cursor.fetchall()
        ticker_id = records[0][0]

        for PDClst in lst:
            PDClst.insert(0, ticker_id)
            tpl = tuple(PDClst)
            sql_insert_Query = "insert into pricedailyclose (tickerid, date, open, high, low, close, adjclose, volume) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_insert_Query, tpl)
            connection.commit()

    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Data inserted into pricedailyclose table"
        closeConnectionAndCursor(connection, cursor, message)

def deleteFromTicker(my_ticker): #Deletes data from ticker table based on specified ticker. 
    try: 
        connection = getConnection()
        sql_delete_Query = "DELETE FROM ticker where ticker = %s"
        cursor = connection.cursor()
        cursor.execute(sql_delete_Query, (my_ticker, ))
        connection.commit()
    
    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Data deleted from ticker table"
        closeConnectionAndCursor(connection, cursor, message)

def insertIntoTicker(my_ticker): #Inserts data from ticker table based on specified ticker. 
    try: 
        connection = getConnection()
        sql_insertIntoTicker_Query = "insert into ticker (ticker) select (%s) where not exists (select ticker from ticker where ticker = (%s)) limit 1;"
        cursor = connection.cursor() 
        cursor.execute(sql_insertIntoTicker_Query, (my_ticker, my_ticker))
        connection.commit()
    
    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Date inserted into ticker table"
        closeConnectionAndCursor(connection, cursor, message)

def getPDCData(my_ticker, startDate, endDate): #Gets data from pricedailyclose table. 
    try: 
        connection = getConnection()
        cursor = connection.cursor()
        sql_select_Query = ("select date, open, high, low, close, adjclose, volume from pricedailyclose p" 
                            " inner join ticker t on t.tickerid = p.tickerid" 
                            " AND t.ticker = (%s) where p.date between (%s) and (%s)")
        cursor.execute(sql_select_Query, (my_ticker, startDate, endDate))
        records = cursor.fetchall()

    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Data retrieved from price daily close table"
        closeConnectionAndCursor(connection, cursor, message)
        return records

def insertIntoSearchHistory(my_ticker, startDate, endDate):
    try: 
        connection = getConnection()
        cursor = connection.cursor()
        sql_insert_Query = "insert into searchhistory (ticker, startdate, enddate) values (%s, %s, %s)"
        cursor.execute(sql_insert_Query, (my_ticker, startDate, endDate))
        connection.commit()

    except Exception as e:
        print("Error reading data: " , e)
    
    finally:
        message = "Data inserted into search history table"
        closeConnectionAndCursor(connection, cursor, message)

# Checks if price data between specified start and end date already exists.
def new_search(my_ticker, startDate, endDate):
    try: 
        connection = getConnection()
        cursor = connection.cursor()
        sql_select_Query = "select count(*) from searchhistory where ticker = (%s) and startdate <= (%s) and enddate >= (%s)"
        cursor.execute(sql_select_Query, (my_ticker, startDate, endDate))
        records = cursor.fetchall()
    
    except Exception as e:
        print("Error reading data: " , e)
    
    finally:
        message = "Data read from search history table"
        closeConnectionAndCursor(connection, cursor, message)
        return records[0][0] == 0
