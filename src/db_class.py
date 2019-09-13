import mysql.connector
from mysql.connector import Error


class DbClass:
    def __init__(self, **db_config):
        try:
            self._conn = mysql.connector.connect(**db_config)
            self._cursor = self._conn.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()
