from flask import Blueprint, request
from databaseConnection import create_connection
from databaseConnection import findPassengersByFlightID
import json


views = Blueprint('passenger_views', __name__)

@views.route('/getPassenger', methods=['POST'])
def getPassenger():
    try:
        conn = create_connection("localhost", 3306, "myDB", "root", "Twistgump1905")
        print("Connection established")
        flight_id = str(request.form.get('flight_id'))
        passengerIDList = findPassengersByFlightID(conn, flight_id)

        
        conn.close()
        print("Connection closed")
        return json.dumps({"passengers": passengerIDList})
    except Exception as e:
        print(f"Error: {e}")
        return str(e)
