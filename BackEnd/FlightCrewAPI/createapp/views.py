from flask import Blueprint, request
from createConnection import create_connection
import json
views = Blueprint('views', __name__)


@views.route('/getFlightCrew', methods=['POST'])
def getFlightCrew():
    connection = create_connection()
    cursor = connection.cursor()
    flightId = request.form.get("flightID")
    cursor.execute(f"""
    SELECT PILOT_ID
    FROM FLIGHTPILOT
    WHERE FLIGHT_ID="{flightId}"
    """)
    data = cursor.fetchall()
    returnList = []
    for pilot in data:
        cursor.execute(
            f"""
            SELECT *
            FROM FLIGHTCREW
            WHERE ID="{pilot[0]}"
            """
        )
        returnList.append(cursor.fetchone())

    cursor.close()
    connection.close()
    return json.dumps(returnList)

