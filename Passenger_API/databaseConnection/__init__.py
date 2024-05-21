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

def findPassengersByFlightID(connection: mysql.connector.connection, flight_id: str) -> list:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT p.ID, p.NAME, p.AGE, p.GENDER, p.NATIONALITY, t.SEAT_NUMBER, t.TYPE
            FROM PassangerInformation p
            LEFT JOIN Ticket t ON p.ID = t.PASSENGER_ID
            WHERE t.FLIGHT_ID = "{flight_id}"
            """
        )
        passengers = cursor.fetchall()

#try comment

        # Enhance data with parent info for infants
        enhanced_passengers = []
        for passenger in passengers:
            passenger_info = {
                "id": passenger[0],
                "name": passenger[1],
                "age": passenger[2],
                "gender": passenger[3],
                "nationality": passenger[4],
                "seat_number": passenger[5],
                "seat_type": passenger[6]
            }
            enhanced_passengers.append(passenger_info)

        return enhanced_passengers
    except Error as e:
        print(f"Error querying MySQL database in function findPassengersByFlightID: {e}")
        return [{"error": str(e)}]