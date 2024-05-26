from databaseConnection import create_connection
import json
from flask import Blueprint, request



views = Blueprint('views', __name__)


@views.route('/getFlightCrew', methods=['GET', 'POST'])
def getFlightCrew():
    connection = create_connection("localhost",3306,"myDB","root","1234")
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
