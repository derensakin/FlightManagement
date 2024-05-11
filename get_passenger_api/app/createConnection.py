# createConnection.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        host = 'localhost'
        port = 3306
        user = 'root'
        password = '1234'
        database = 'myDB'
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")