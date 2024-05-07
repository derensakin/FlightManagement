from flask import Flask
import mysql.connector
from mysql.connector import Error
from flask import Blueprint, request
import json


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


views = Blueprint('views', __name__)


@views.route('/getFlightCrew', methods=['GET', 'POST'])
def getFlightCrew():
    connection = create_connection()
    cursor = connection.cursor()
    flightId = request.form.get("flightID")
    print(flightId)
    # flightId = "CS1031"
    cursor.execute(f"""
    SELECT PILOT_ID
    FROM FLIGHTPILOT
    WHERE FLIGHT_ID="{flightId}"
    """)
    data = cursor.fetchall()
    returnList = []
    for mPilot in data:
        cursor.execute(
            f"""
            SELECT *
            FROM FLIGHTCREW
            WHERE ID="{mPilot[0]}"
            """
        )
        pilot = cursor.fetchone()
        cursor.execute(
            f"""
            SELECT LANGUAGE
            FROM FLIGHTCREWKNOWNLANGUAGES
            WHERE ID="{mPilot[0]}"
            """
        )
        languages = []
        output = cursor.fetchall()
        for language in output:
            languages.append(language[0])
        returnList.append(
            {"ID": pilot[0], "Name": pilot[1], "Age": pilot[2], "Gender": pilot[3], "Nationality": pilot[4],
             "Vehicle": pilot[5], "Seniority": pilot[6], "Max_Distance": pilot[7], "Languages": languages})


    cursor.close()
    connection.close()
    return json.dumps(returnList)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Sacred_Key"
    app.register_blueprint(views, url_prefix="/")

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
