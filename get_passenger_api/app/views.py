# views.py
from flask import Blueprint, request
from createConnection import create_connection
from flask import jsonify

views = Blueprint('passenger_views', __name__)

@views.route('/getPassengers', methods=['GET'])
def get_passengers():
    connection = create_connection()
    cursor = connection.cursor()
    flight_id = request.args.get("flightID")
    cursor.execute(
        f"""
        SELECT PASSENGER_ID, NAME, AGE, GENDER, NATIONALITY, SEAT_TYPE, SEAT_NUMBER
        FROM PASSENGERS
        WHERE FLIGHT_ID="{flight_id}"
        """
    )
    passengers = cursor.fetchall()
    return_list = []
    for passenger in passengers:
        passenger_info = {
            "ID": passenger[0],
            "Name": passenger[1],
            "Age": passenger[2],
            "Gender": passenger[3],
            "Nationality": passenger[4],
            "Seat Type": passenger[5],
            "Seat Number": passenger[6]
        }
        return_list.append(passenger_info)
    cursor.close()
    connection.close()
    return jsonify(return_list)
