from server.models.connection import get_connection, close_connection_and_cursor
from server.config.serverInfo import DB_DATABASE

class Database:
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
        self.execute_query(query, error_msg="Error creating database: ", success_msg="Database created", database_exists=False)

    def drop_database(self):
        query = "drop database if exists " + self.database
        self.execute_query(query, error_msg="Error dropping database: ", success_msg="Database dropped", database_exists=False)

    def create_ticker_table(self):
        query = "create table if not exists `" + self.database + "`.`ticker` (`tickerid` int not null auto_increment, `ticker` varchar(45) not null, primary key (`tickerid`))"
        self.execute_query(query, error_msg="Error creating ticker table: ", success_msg="Ticker table created", database_exists=True)

    def drop_ticker_table(self):
        query = "drop table if exists `" + self.database + "`.`ticker`"
        self.execute_query(query, error_msg="Error dropping ticker table: ", success_msg="Ticker table dropped", database_exists=True)

    def create_PDC_table(self):
        query = "create table if not exists `" + self.database + "`.`pricedailyclose` (`tickerid` int not null, `date` datetime not null, `close` decimal(12, 4) null, `high` decimal(12, 4) null, `low` decimal(12, 4) null, `open` decimal(12, 4) null, `volume` decimal(20, 2) null, primary key (`tickerid`, `date`))"
        self.execute_query(query, error_msg="Error creating price daily close table: ", success_msg="Price daily close table created", database_exists=True)

    def drop_PDC_table(self):
        query = "drop table if exists " + self.database + "`.`pricedailyclose`"
        self.execute_query(query, error_msg="Error dropping price daily close table: ", success_msg="Price daily close table dropped", database_exists=True)

    def create_search_history_table(self):
        query = "create table if not exists `" + self.database + "`.`searchhistory` (`ticker` varchar(45) not null, `startdate` datetime not null, `enddate` datetime not null)"
        self.execute_query(query, error_msg="Error creating search history table: ", success_msg="Search history table created", database_exists=True)

    def drop_search_history_table(self):
        query = "drop table if exists `" + self.database + "`.`searchhistory`"
        self.execute_query(query, error_msg="Error dropping search history table: ", success_msg="Search history table dropped", database_exists=True)

def teardown_DB():
    db = Database()
    db.drop_PDC_table()
    db.drop_ticker_table()
    db.drop_search_history_table()
    db.drop_database()

def build_DB():
    db = Database()
    db.create_database()
    db.create_search_history_table()
    db.create_ticker_table()
    db.create_PDC_table()

if __name__ == '__main__':
    build_DB()
