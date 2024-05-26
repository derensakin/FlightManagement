from flask import Blueprint, request, jsonify
from DBconnection import create_connection, findFlightByID, findFlightsAdvanced, findTicketsByFlightID, findFlightPilotsByFlightID
import json

views = Blueprint('views', __name__)

views = Blueprint('views', __name__)


@views.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    conn = create_connection("localhost",3306,"myDB","root", 'password')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = \"{username}\"")
    data = cursor.fetchone()
    if data[1] == password:
        return jsonify({'status': 'success', 'data': [data[0],data[2]]}), 200
    else:
        return jsonify({'status': 'fail'}), 401


@views.route('/getFlight', methods=['POST'])
def getFlight():
    try:
        flightID = request.form.get('flightID')  
        conn = create_connection("localhost", 3306, "database_name", "user", "password")
        flightDetails = findFlightByID(conn, flightID)
        conn.close()
        if flightDetails:
            return jsonify({
                "id": flightDetails[0],
                "departure_date": flightDetails[1].strftime("%Y-%m-%d %H:%M:%S"),
                "duration": flightDetails[2],
                "distance": flightDetails[3],
                "source_country": flightDetails[4],
                "source_city": flightDetails[5],
                "source_airport": flightDetails[6],
                "source_airport_code": flightDetails[7],
                "vehicle": flightDetails[8],
                "shared_flight": flightDetails[9]
            })
        else:
            return jsonify({"error": "Flight not found"}), 404
    except Exception as e:
        print(e)
        return str(e), 500

@views.route('/searchFlights', methods=['POST'])
def searchFlights():
    try:
        data = request.get_json()
        filters = {
            'id': data.get('id'),
            'departure_date': data.get('departure_date'),
            'duration': data.get('duration'),
            'distance': data.get('distance'),
            'source_country': data.get('source_country'),
            'source_city': data.get('source_city'),
            'source_airport': data.get('source_airport'),
            'source_airport_code': data.get('source_airport_code'),
            'vehicle': data.get('vehicle'),
            'shared_flight': data.get('shared_flight')
        }

        filters = {k: v for k, v in filters.items() if v is not None}

        conn = create_connection("localhost", 3306, "database_name", "user", "password")
        flights = findFlightsAdvanced(conn, filters)
        conn.close()

        results = [{
            "id": flight[0],
            "departure_date": flight[1].strftime("%Y-%m-%d %H:%M:%S"),
            "duration": flight[2],
            "distance": flight[3],
            "source_country": flight[4],
            "source_city": flight[5],
            "source_airport": flight[6],
            "source_airport_code": flight[7],
            "vehicle": flight[8],
            "shared_flight": flight[9]
        } for flight in flights]

        return jsonify(results)
    except Exception as e:
        print(e)
        return str(e), 500

@views.route('/getTicketsByFlight', methods=['POST'])
def getTicketsByFlight():
    try:
        flightID = request.form.get('flightID')
        conn = create_connection("localhost", 3306, "database_name", "user", "password")
        tickets = findTicketsByFlightID(conn, flightID)
        conn.close()
        ticket_list = [{"ticket_id": ticket[0], "seat_number": ticket[1], "type": ticket[2], "passenger_id": ticket[3]} for ticket in tickets]
        return jsonify(ticket_list)
    except Exception as e:
        print(e)
        return str(e), 500

@views.route('/getFlightPilotsByFlight', methods=['POST'])
def getFlightPilotsByFlight():
    try:
        flightID = request.form.get('flightID')
        conn = create_connection("localhost", 3306, "database_name", "user", "password")
        pilots = findFlightPilotsByFlightID(conn, flightID)
        conn.close()
        pilot_list = [{"flight_id": pilot[0], "pilot_id": pilot[1]} for pilot in pilots]
        return jsonify(pilot_list)
    except Exception as e:
        print(e)
        return str(e), 500
