from connection import get_connection, close_connection_and_cursor
from serverInfo import DB_DATABASE

class DatabaseBuild:
    def __init__(self):
        self.database = DB_DATABASE

    def execute_query(self, query, error_msg="Error reading data: ", success_msg="Query succeeded", database_exists=False):
        try:
            connection = get_connection(self.database, database_exists)
            cursor = connection.cursor()
            cursor.execute(query)

        except Exception as e:
            print(error_msg, e)

        finally:
            close_connection_and_cursor(connection, cursor, success_msg)

    def create_database(self):
        query = "create database if not exists " + self.database
        self.execute_query(query, errorMsg="Error creating database: ", successMsg="Database created", databaseExists=False)

    def drop_database(self):
        query = "drop database if not exists " + self.database
        self.execute_query(query, errorMsg="Error dropping database: ", successMsg="Database dropped", databaseExists=False)

    def create_ticker_table(self):
        query = "create table if not exists `" + self.database + "`.`ticker` (`tickerid` int not null auto_increment, `ticker` varchar(45) not null, primary key (`tickerid`))"
        self.execute_query(query, errorMsg="Error creating ticker table: ", successMsg="Ticker table created", databaseExists=True)

    def drop_ticker_table(self):
        query = "drop table if not exists `" + self.database + "`.`ticker`"
        self.execute_query(query, errorMsg="Error dropping ticker table: ", successMsg="Ticker table dropped", databaseExists=True)

    def create_PDC_table(self):
        query = "create table if not exists `" + self.database + "`.`pricedailyclose` (`tickerid` int not null, `date` datetime not null, `open` decimal(12, 4) null, `high` decimal(12, 4) null, `low` decimal(12, 4) null, `close` decimal(12, 4) null, `adjclose` decimal(12, 4) null, `volume` decimal(20, 2) null, primary key (`tickerid`, `date`))"
        self.execute_query(query, errorMsg="Error creating price daily close table: ", successMsg="Price daily close table created", databaseExists=True)

    def drop_PDC_table(self):
        query = "drop table if exists " + self.database + "`.`pricedailyclose`"
        self.execute_query(query, errorMsg="Error dropping price daily close table: ", successMsg="Price daily close table dropped", databaseExists=True)

    def create_search_history_table(self):
        query = "create table if not exists `" + self.database + "`.`searchhistory` (`ticker` varchar(45) not null, `startdate` datetime not null, `enddate` datetime not null)"
        self.execute_query(query, errorMsg="Error creating search history table: ", successMsg="Search history table created", databaseExists=True)

    def drop_search_history_table(self):
        query = "drop table if exists `" + self.database + "`.`searchhistory`"
        self.execute_query(query, errorMsg="Error dropping search history table: ", successMsg="Search history table dropped", databaseExists=True)

def build_DB():
    db = DatabaseBuild()
    db.create_database()
    db.create_search_history_table()
    db.create_ticker_table()
    db.create_PDC_table()

if __name__ == '__main__':
    build_DB()
