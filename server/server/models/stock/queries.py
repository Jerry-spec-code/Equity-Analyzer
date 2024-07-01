from server.models.connection import get_connection, close_connection_and_cursor

def delete_PDC(my_ticker, start_date, end_date): #Deletes data between specified start and end date.
    try: 
        connection = get_connection()
        sql_delete_query = "DELETE p FROM pricedailyclose p inner join ticker t on t.tickerid = p.tickerid AND t.ticker = (%s) where p.date between (%s) and (%s)"
        cursor = connection.cursor()
        cursor.execute(sql_delete_query, (my_ticker, start_date, end_date))
        connection.commit()
    
    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Data deleted from price daily close table"
        close_connection_and_cursor(connection, cursor, message)

def insert_PDC(my_ticker, lst): #inserts data into price daily close table 
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = "select tickerid from ticker where ticker = (%s)"
        cursor.execute(sql_select_query, (my_ticker, ))
        records = cursor.fetchall()
        ticker_id = records[0][0]

        for PDClst in lst:
            PDClst.insert(0, ticker_id)
            tpl = tuple(PDClst)
            sql_insert_query = "insert into pricedailyclose (tickerid, date, open, high, low, close, adjclose, volume) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_insert_query, tpl)
            connection.commit()

    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Data inserted into price daily close table"
        close_connection_and_cursor(connection, cursor, message)

def delete_ticker(my_ticker): #Deletes data from ticker table based on specified ticker. 
    try: 
        connection = get_connection()
        sql_delete_query = "DELETE FROM ticker where ticker = %s"
        cursor = connection.cursor()
        cursor.execute(sql_delete_query, (my_ticker, ))
        connection.commit()
    
    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Data deleted from ticker table"
        close_connection_and_cursor(connection, cursor, message)

def insert_ticker(my_ticker): #Inserts data from ticker table based on specified ticker. 
    try: 
        connection = get_connection()
        sql_insert_query = "insert into ticker (ticker) select (%s) where not exists (select ticker from ticker where ticker = (%s)) limit 1;"
        cursor = connection.cursor() 
        cursor.execute(sql_insert_query, (my_ticker, my_ticker))
        connection.commit()
    
    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Date inserted into ticker table"
        close_connection_and_cursor(connection, cursor, message)

def get_pdc_data(my_ticker, start_date, end_date): #Gets data from pricedailyclose table. 
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = ("select date, open, high, low, close, adjclose, volume from pricedailyclose p" 
                            " inner join ticker t on t.tickerid = p.tickerid" 
                            " AND t.ticker = (%s) where p.date between (%s) and (%s)")
        cursor.execute(sql_select_query, (my_ticker, start_date, end_date))
        records = cursor.fetchall()

    except Exception as e:
        print("Error reading data: " , e)

    finally:
        message = "Data retrieved from price daily close table"
        close_connection_and_cursor(connection, cursor, message)
        return records

def insert_search_history(my_ticker, start_date, end_date):
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        sql_insert_query = "insert into searchhistory (ticker, startdate, enddate) values (%s, %s, %s)"
        cursor.execute(sql_insert_query, (my_ticker, start_date, end_date))
        connection.commit()

    except Exception as e:
        print("Error reading data: " , e)
    
    finally:
        message = "Data inserted into search history table"
        close_connection_and_cursor(connection, cursor, message)

# Checks if price data between specified start and end date already exists.
def not_queried_before(my_ticker, start_date, end_date):
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = "select count(*) from searchhistory where ticker = (%s) and startdate <= (%s) and enddate >= (%s)"
        cursor.execute(sql_select_query, (my_ticker, start_date, end_date))
        records = cursor.fetchall()
    
    except Exception as e:
        print("Error reading data: " , e)
    
    finally:
        message = "Data read from search history table"
        close_connection_and_cursor(connection, cursor, message)
        return records[0][0] == 0
