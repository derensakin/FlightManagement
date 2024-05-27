from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

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

passenger_api = Blueprint('passenger_api', __name__)

def assign_seat(passenger_id, flight_id):
    connection = create_connection()
    cursor = connection.cursor(buffered=True)

    # Check if the passenger is an infant
    cursor.execute(
        "SELECT age, parent_id FROM PASSENGERS WHERE passenger_id=%s", (passenger_id,)
    )
    passenger_info = cursor.fetchone()
    if passenger_info and passenger_info[0] <= 2:
        # If the passenger is an infant, check the parent's seat
        cursor.execute(
            "SELECT seat_number FROM PASSENGERS WHERE passenger_id=%s", (passenger_info[1],)
        )
        parent_seat = cursor.fetchone()
        cursor.close()
        connection.close()
        return parent_seat[0] if parent_seat else None  # Assume parent always has a seat; handle otherwise

    # For other passengers, find and assign the first available seat
    cursor.execute(
        "SELECT seat_number FROM SEATS WHERE flight_id=%s AND available=True LIMIT 1", (flight_id,)
    )
    seat_number = cursor.fetchone()
    if seat_number:
        cursor.execute(
            "UPDATE SEATS SET available=False WHERE seat_number=%s AND flight_id=%s",
            (seat_number[0], flight_id)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return seat_number[0]

    cursor.close()
    connection.close()
    return None  # Handle cases where no seats are available

@passenger_api.route('/getPassengers', methods=['GET'])
def get_passengers():
    connection = create_connection()
    cursor = connection.cursor()
    flight_id = request.args.get("flightID")

    cursor.execute(
        """
        SELECT PASSENGER_ID, NAME, AGE, GENDER, NATIONALITY, SEAT_TYPE, SEAT_NUMBER
        FROM PASSENGERS
        WHERE FLIGHT_ID=%s
        """, (flight_id,)
    )
    passengers = cursor.fetchall()
    return_list = []
    for passenger in passengers:
        seat_number = passenger[6] or assign_seat(passenger[0], flight_id)
        passenger_info = {
            "ID": passenger[0],
            "Name": passenger[1],
            "Age": passenger[2],
            "Gender": passenger[3],
            "Nationality": passenger[4],
            "Seat Type": passenger[5],
            "Seat Number": seat_number
        }
        return_list.append(passenger_info)

    cursor.close()
    connection.close()
    return jsonify(return_list)

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Another_Secret_Key"
    app.register_blueprint(passenger_api, url_prefix="/passenger")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)