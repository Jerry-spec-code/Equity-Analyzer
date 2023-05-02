from connection import getConnection, closeConnectionAndCursor
from serverInfo import DB_DATABASE

class DatabaseBuild:
    def __init__(self):
        self.database = DB_DATABASE

    def executeQuery(self, query, errorMsg="Error reading data: ", successMsg="Query succeeded", databaseExists=False):
        try:
            connection = getConnection(self.database, databaseExists)
            cursor = connection.cursor()
            cursor.execute(query)

        except Exception as e:
            print(errorMsg, e)

        finally:
            closeConnectionAndCursor(connection, cursor, successMsg)

    def createDatabase(self):
        query = "create database if not exists " + self.database
        self.executeQuery(query, errorMsg="Error creating database: ", successMsg="Database created", databaseExists=False)

    def dropDatabase(self):
        query = "drop database if not exists " + self.database
        self.executeQuery(query, errorMsg="Error dropping database: ", successMsg="Database dropped", databaseExists=False)

    def createTickerTable(self):
        query = "create table if not exists `" + self.database + "`.`ticker` (`tickerid` int not null auto_increment, `ticker` varchar(45) not null, primary key (`tickerid`))"
        self.executeQuery(query, errorMsg="Error creating ticker table: ", successMsg="Ticker table created", databaseExists=True)

    def dropTickerTable(self):
        query = "drop table if not exists `" + self.database + "`.`ticker`"
        self.executeQuery(query, errorMsg="Error dropping ticker table: ", successMsg="Ticker table dropped", databaseExists=True)

    def createPDCTable(self):
        query = "create table if not exists `" + self.database + "`.`pricedailyclose` (`tickerid` int not null, `date` datetime not null, `open` decimal(12, 4) null, `high` decimal(12, 4) null, `low` decimal(12, 4) null, `close` decimal(12, 4) null, `adjclose` decimal(12, 4) null, `volume` decimal(20, 2) null, primary key (`tickerid`, `date`))"
        self.executeQuery(query, errorMsg="Error creating price daily close table: ", successMsg="Price daily close table created", databaseExists=True)

    def dropPDCTable(self):
        query = "drop table if exists " + self.database + "`.`pricedailyclose`"
        self.executeQuery(query, errorMsg="Error dropping price daily close table: ", successMsg="Price daily close table dropped", databaseExists=True)

    def createSearchHistoryTable(self):
        query = "create table if not exists `" + self.database + "`.`searchhistory` (`ticker` varchar(45) not null, `startdate` datetime not null, `enddate` datetime not null)"
        self.executeQuery(query, errorMsg="Error creating search history table: ", successMsg="Search history table created", databaseExists=True)

    def dropSearchHistoryTable(self):
        query = "drop table if exists `" + self.database + "`.`searchhistory`"
        self.executeQuery(query, errorMsg="Error dropping search history table: ", successMsg="Search history table dropped", databaseExists=True)

def buildDB():
    db = DatabaseBuild()
    db.createDatabase()
    db.createSearchHistoryTable()
    db.createTickerTable()
    db.createPDCTable()

if __name__ == '__main__':
    buildDB()
