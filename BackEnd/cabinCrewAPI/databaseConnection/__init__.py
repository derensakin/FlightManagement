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

def findCabinCrewsWithID(connection: mysql.connector.connection, id: int) -> list:
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM CABINCREW WHERE ID = {id}")
        reutrnList = cursor.fetchone()

        return reutrnList
    except Error as e:
        print(f"Error connecting to MySQL database in function findCabinCrew: {e}")

def findCabinCrewIDs(connection: mysql.connector.connection, id: str) -> list:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT CABIN_CREW_ID FROM FLIGHTCABINCREW WHERE FLIGHT_ID = "{id}"
            """
        )
        reutrnList = cursor.fetchall()
        return reutrnList
    except Error as e:
        print(f"Error connecting to MySQL database in function findCabinCrewIDs: {e}")

def findCabinCrewLanguagesWithID(connection: mysql.connector.connection, id: int) -> list:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT LANGUAGE FROM CABINCREWKNOWNLANGUAGES WHERE ID = {id}
            """
        )
        return cursor.fetchall()
    except Error as e:
        print(f"Error connecting to MySQL database in function findCabinCrewLanguagesWithID: {e}")


def getMealsWithID(connection: mysql.connector.connection, id: int) -> list:
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT FOOD
            FROM CABINCREWFOOD
            WHERE CABIN_CREW_ID = {id}
            """
        )
        list = cursor.fetchall()
        return list
    except Error as e:
        print(f"Error connecting to MySQL database in function getMealsWithID: {e}")

