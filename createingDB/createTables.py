import mysql.connector
from mysql.connector import Error


def create_connection(host, port, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        print("Connection to MySQL successful")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_flight_crew_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS FlightCrew (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NAME VARCHAR(50),
                AGE INT,
                GENDER VARCHAR(10),
                NATIONALITY VARCHAR(50),
                VEHICLE VARCHAR(50),
                SENIORITY VARCHAR(50),
                FLIGHT_RANGE INT
            );
            """
        )
        print("Table 'FlightCrew' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def create_flight_crew_known_languages_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS FlightCrewKnownLanguages (
                ID INT,
                LANGUAGE VARCHAR(50),
                PRIMARY KEY(ID,LANGUAGE),
                FOREIGN KEY(ID) REFERENCES FlightCrew(ID)
            )
            """
        )
        print("Table 'FlightCrewKnownLanguages' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def create_cabin_crew_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS CabinCrew (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(50),
            AGE INT,
            GENDER VARCHAR(10),
            NATIONALITY VARCHAR(80),
            TYPE VARCHAR(50),
            VEHİCLE VARCHAR(50)
            )
            """
        )
        print("Table 'CabinCrew' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def create_cabin_crew_known_languages_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS CabinCrewKnownLanguages (
            ID INT,
            LANGUAGE VARCHAR(50),
            PRIMARY KEY(ID,LANGUAGE),
            FOREIGN KEY(ID) REFERENCES CabinCrew(ID)
            )
            """
        )
        print("Table 'CabinCrewKnownLanguages' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def create_passanger_information_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS PassangerInformation (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(50),
            AGE INT,
            GENDER VARCHAR(10),
            NATIONALITY VARCHAR(50)
            )
            """
        )
        print("Table 'PassangerInformation' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def create_flight_information_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS FlightInformation (
            ID VARCHAR(6) PRIMARY KEY,
            DEPARTURE_DATE DATETIME,
            DURATION INT,
            DISTANCE INT,
            SOURCE_COUNTRY VARCHAR(80),
            SOURCE_CITY VARCHAR(80),
            SOURCE_AIRPORT VARCHAR(80),
            SOURCE_AIRPORT_CODE VARCHAR(3),
            VEHICLE VARCHAR(50),
            SHARED_FLIGHT VARCHAR(6)


            )
            """
        )
        print("Table 'FlightInformation' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def create_ticket_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Ticket (
            FLIGHT_ID VARCHAR(6),
            SEAT_NUMBER INT,
            TYPE VARCHAR(50),
            PASSENGER_ID INT,
            PRIMARY KEY(FLIGHT_ID,PASSENGER_ID),
            FOREIGN KEY(FLIGHT_ID) REFERENCES FlightInformation(ID),
            FOREIGN KEY(PASSENGER_ID) REFERENCES PassangerInformation(ID)
            )
            """
        )
        print("Table 'Ticket' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def create_flight_pilot_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS FlightPilot (
            FLIGHT_ID VARCHAR(6),
            PILOT_ID INT,
            PRIMARY KEY(FLIGHT_ID,PILOT_ID),
            FOREIGN KEY(FLIGHT_ID) REFERENCES FlightInformation(ID),
            FOREIGN KEY(PILOT_ID) REFERENCES FlightCrew(ID)
            )
            """
        )
        print("Table 'FlightPilot' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def create_flight_cabin_crew_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS FlightCabinCrew (
            FLIGHT_ID VARCHAR(6),
            CABIN_CREW_ID INT,
            PRIMARY KEY(FLIGHT_ID,CABIN_CREW_ID),
            FOREIGN KEY(FLIGHT_ID) REFERENCES FlightInformation(ID),
            FOREIGN KEY(CABIN_CREW_ID) REFERENCES CabinCrew(ID)
            )
            """
        )
        print("Table 'FlightCabinCrew' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def cabin_crew_food_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS CabinCrewFood (
            CABIN_CREW_ID INT,
            FOOD VARCHAR(50),
            PRIMARY KEY(CABIN_CREW_ID,FOOD),
            FOREIGN KEY(CABIN_CREW_ID) REFERENCES CabinCrew(ID)

            )
            """
        )
        print("Table 'CabinCrewFood' created successfully")
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def main():
    host = 'localhost'
    port = 3306
    user = 'root'
    password = '1234'
    database = 'myDB'

    connection = create_connection(host, port, user, password, database)
    if connection:
        create_flight_crew_table(connection)
        create_cabin_crew_table(connection)
        create_cabin_crew_known_languages_table(connection)
        create_flight_crew_known_languages_table(connection)
        create_passanger_information_table(connection)
        create_flight_information_table(connection)
        create_ticket_table(connection)
        create_flight_pilot_table(connection)
        create_flight_cabin_crew_table(connection)
        cabin_crew_food_table(connection)

        connection.close()


if __name__ == '__main__':
    main()



