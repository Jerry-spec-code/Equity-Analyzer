import mysql.connector

import serverInfo as s 

def createDatabase():
    try:
        connection = mysql.connector.connect(host = s.host,
        user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute("create database if not exists " + s.database)

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("Database created")

def dropDatabase():
    try:
        connection = mysql.connector.connect(host = s.host,
        user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute("drop database if exists " + s.database)

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("Database dropped")

def createTickerTable():
    try:
        connection = mysql.connector.connect(host = s.host,
        database = s.database, user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute("create table if not exists `" + s.database + "`.`ticker` (`tickerid` int not null auto_increment, `ticker` varchar(45) not null, primary key (`tickerid`))")

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("Ticker table created")

def dropTickerTable():
    try:
        connection = mysql.connector.connect(host = s.host,
        database = s.database, user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute("drop table if exists `ticker`")

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("Ticker table dropped")

def createPDCTable():
    try:
        connection = mysql.connector.connect(host = s.host,
        database = s.database, user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute("create table if not exists `" + s.database + "`.`pricedailyclose` (`tickerid` int not null, `date` datetime not null, `open` decimal(12, 4) null, `high` decimal(12, 4) null, `low` decimal(12, 4) null, `close` decimal(12, 4) null, `adjclose` decimal(12, 4) null, `volume` decimal(20, 2) null, primary key (`tickerid`, `date`))")

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("price daily close table created")

def dropPDCTable():
    try:
        connection = mysql.connector.connect(host = s.host,
        database = s.database, user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute("drop table if exists `pricedailyclose`")

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("price daily close table dropped")

def createSearchHistoryTable():
    try:
        connection = mysql.connector.connect(host = s.host,
        database = s.database, user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute("create table if not exists `" + s.database + "`.`searchhistory` (`ticker` varchar(45) not null, `startdate` datetime not null, `enddate` datetime not null)")

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("search history table created")

def dropSearchHistoryTable():
    try:
        connection = mysql.connector.connect(host = s.host,
        database = s.database, user= s.user, password = s.password)
        cursor = connection.cursor()
        cursor.execute("drop table if exists `search history`")

    except mysql.connector.Error as e:
        print("Error reading data: " , e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("search history table dropped")

def buildDB():
    createDatabase()
    createSearchHistoryTable()
    createTickerTable()
    createPDCTable()

