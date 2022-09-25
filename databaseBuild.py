import mysql.connector
import serverInfo as s 

def executeQuery(query, errorMsg="Error reading data: ", successMsg="Query succeeded", databaseExists=False):
    try:
        connection = ""
        if databaseExists:
            connection = mysql.connector.connect(host = s.host,
            database = s.database, user= s.user, password = s.password)            
        else:
            connection = mysql.connector.connect(host = s.host,
            user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute(query)

    except mysql.connector.Error as e:
        print(errorMsg, e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print(successMsg) 

def createDatabase():
    query = "create database if not exists " + s.database
    executeQuery(query, errorMsg="Error creating database: ", successMsg="Database created", databaseExists=False)

def dropDatabase():
    query = "drop database if not exists " + s.database
    executeQuery(query, errorMsg="Error dropping database: ", successMsg="Database dropped", databaseExists=False)

def createTickerTable():
    query = "create table if not exists `" + s.database + "`.`ticker` (`tickerid` int not null auto_increment, `ticker` varchar(45) not null, primary key (`tickerid`))"
    executeQuery(query, errorMsg="Error creating ticker table: ", successMsg="Ticker table created", databaseExists=True)

def dropTickerTable():
    query = "drop table if not exists `" + s.database + "`.`ticker`"
    executeQuery(query, errorMsg="Error dropping ticker table: ", successMsg="Ticker table dropped", databaseExists=True)

def createPDCTable():
    query = "create table if not exists `" + s.database + "`.`pricedailyclose` (`tickerid` int not null, `date` datetime not null, `open` decimal(12, 4) null, `high` decimal(12, 4) null, `low` decimal(12, 4) null, `close` decimal(12, 4) null, `adjclose` decimal(12, 4) null, `volume` decimal(20, 2) null, primary key (`tickerid`, `date`))"
    executeQuery(query, errorMsg="Error creating price daily close table: ", successMsg="Price daily close table created", databaseExists=True)

def dropPDCTable():
    query = "drop table if exists " + s.database + "`.`pricedailyclose`"
    executeQuery(query, errorMsg="Error dropping price daily close table: ", successMsg="Price daily close table dropped", databaseExists=True)

def createSearchHistoryTable():
    query = "create table if not exists `" + s.database + "`.`searchhistory` (`ticker` varchar(45) not null, `startdate` datetime not null, `enddate` datetime not null)"
    executeQuery(query, errorMsg="Error creating search history table: ", successMsg="Search history table created", databaseExists=True)

def dropSearchHistoryTable():
    query = "drop table if exists `" + s.database + "`.`searchhistory`"
    executeQuery(query, errorMsg="Error dropping search history table: ", successMsg="Search history table dropped", databaseExists=True)

def buildDB():
    createDatabase()
    createSearchHistoryTable()
    createTickerTable()
    createPDCTable()

buildDB()
