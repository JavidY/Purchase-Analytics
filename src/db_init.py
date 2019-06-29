import mysql.connector
from mysql.connector import errorcode


config = {
    'user': 'pa_oltp',
    'password': 'mypassword',
    'host': '127.0.0.1',
    'port': '3306',
    'raise_on_warnings': True
}


def connect_db():
    """A connect function returning mysql connection object.
    Connection arguments(username,pass,host,.etc)
    are passed inside the function"""
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something wrong with your username or password")
            raise err
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            raise err
        else:
            print(err)
            raise err


cnx = connect_db()
print("Success")
