import mysql.connector
import server.config.serverInfo as s

def get_connection(database=s.DB_DATABASE, database_exists=True):
    if database_exists:
        return mysql.connector.connect(host = s.DB_HOST,
            database = database, user = s.DB_USER, password = s.DB_PASSWORD)
    else:
        return mysql.connector.connect(host = s.DB_HOST,
            user = s.DB_USER, password = s.DB_PASSWORD)

def close_connection_and_cursor(connection, cursor, message):
    if connection.is_connected(): 
        connection.close()
        cursor.close()
        print(message)