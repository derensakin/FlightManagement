from flask import Blueprint, request
from databaseConnection import create_connection
from databaseConnection import findPassengersByFlightID
from databaseConnection import change_seats
import json


views = Blueprint('passenger_views', __name__)

@views.route('/getPassenger', methods=['POST'])
def getPassenger():
    try:
        conn = create_connection("localhost", 3306, "myDB", "root", "****")
        print("Connection established")
        flight_id = str(request.form.get('flight_id'))
        passengerIDList = findPassengersByFlightID(conn, flight_id)

        
        conn.close()
        print("Connection closed")
        return json.dumps({"passengers": passengerIDList})
    except Exception as e:
        print(f"Error: {e}")
        return str(e)

@views.route('/changeSeats', methods=['POST'])
def changeSeats():
    try:
        conn = create_connection("localhost", 3306, "myDB", "root", "****")
        print("Connection established")
        flight_id = str(request.form.get('flight_id'))
        passenger_id1 = int(request.form.get('passenger_id1'))
        passenger_id2 = int(request.form.get('passenger_id2'))
        if change_seats(conn, passenger_id1, passenger_id2, flight_id):
            conn.close()
            return json.dumps({"status": "success"})

        conn.close()

        return json.dumps({"status": "fail"})
    except Exception as e:
        print(f"Error: {e}")
        return json.dumps({"status": "fail"})



