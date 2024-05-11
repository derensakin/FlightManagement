import mysql.connector
from mysql.connector import Error


def create_connection(host: str, port: int, database: str, user: str, password: str) -> mysql.connector.connection:
    try:
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
        
def findFlightByID(connection: mysql.connector.connection, id: str) -> list:
    
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM FLIGHTINFORMATION WHERE ID = '{id}'")
        return cursor.fetchone()
    except Error as e:
        print(f"Error finding flight by ID in MySQL database: {e}")

def findAllFlights(connection: mysql.connector.connection) -> list:
   
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM FLIGHTINFORMATION")
        return cursor.fetchall()
    except Error as e:
        print(f"Error finding all flights in MySQL database: {e}")

def findFlightsByCountry(connection: mysql.connector.connection, country: str) -> list:
    
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM FLIGHTINFORMATION WHERE SOURCE_COUNTRY = '{country}' OR DESTINATION_COUNTRY = '{country}'")
        return cursor.fetchall()
    except Error as e:
        print(f"Error finding flights by country in MySQL database: {e}")