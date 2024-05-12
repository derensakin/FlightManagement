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
        
def findFlightsAdvanced(connection: mysql.connector.connection, filters: dict) -> list:
    base_query = "SELECT * FROM FLIGHTINFORMATION"
    conditions = []
    params = []
    
    
    # Dinamik sorgu 
    for field, value in filters.items():
        if value:
            conditions.append(f"{field} = %s")
            params.append(value)

    if conditions:
        query = f"{base_query} WHERE {' AND '.join(conditions)}"
    else:
        query = base_query  #filtre yoksa tüm kayıtlar

    try:
        cursor = connection.cursor()
        cursor.execute(query, tuple(params))
        return cursor.fetchall()
    except Error as e:
        print(f"Error executing query in findFlightsAdvanced: {e}")
        return []

def findTicketsByFlightID(connection: mysql.connector.connection, flight_id: str) -> list:
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM TICKET WHERE FLIGHT_ID = %s", (flight_id,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error finding tickets by flight ID in MySQL database: {e}")

def findFlightPilotsByFlightID(connection: mysql.connector.connection, flight_id: str) -> list:
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM FLIGHTPILOT WHERE FLIGHT_ID = %s", (flight_id,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error finding flight pilots by flight ID in MySQL database: {e}")
