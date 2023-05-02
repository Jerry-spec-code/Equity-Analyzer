import mysql.connector
import serverInfo as s

def getConnection(database=s.DB_DATABASE, databaseExists=True):
    if databaseExists:
        return mysql.connector.connect(host = s.DB_HOST,
            database = database, user = s.DB_USER, password = s.DB_PASSWORD)
    else:
        return mysql.connector.connect(host = s.DB_HOST,
            user = s.DB_USER, password = s.DB_PASSWORD)

def closeConnectionAndCursor(connection, cursor, message):
    if connection.is_connected(): 
        connection.close()
        cursor.close()
        print(message)