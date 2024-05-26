import mysql.connector
from mysql.connector import Error
from faker import Faker
import random
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


def create_users_table(connection: mysql.connector.connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL,
            userType varchar(20) NOT NULL            
            )
            """
        )
        connection.commit()
        print("User table created successfully")
    except Error as e:
        print(f"Error creating table: {e}")


def create_fake_users(connection: mysql.connector.connection):
    try:
        cursor = connection.cursor()
        myFaker = Faker()
        for _ in range(100):
            username = myFaker.user_name()
            password = myFaker.password()
            userType = random.choice(["flightCrew", "cabinCrew", "passanger",])
            cursor.execute("INSERT INTO users (username, password, userType) VALUES (%s, %s, %s)", (username, password, userType))
            connection.commit()

        username = "admin"
        password = "pass"
        userType = "admin"
        cursor.execute("INSERT INTO users (username, password, userType) VALUES (%s, %s, %s)",(username, password, userType))
        connection.commit()
        print("Fake users created successfully")
    except Error as e:
        print(f"Error creating fake users: {e}")


def main():
    connection = create_connection(
        host="localhost",
        port=3306,
        user="root",
        password='password',
        database="myDB"
    )
    create_users_table(connection)
    create_fake_users(connection)

if __name__ == "__main__":
    main()
