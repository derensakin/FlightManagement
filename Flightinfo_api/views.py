from flask import Blueprint, request, jsonify
from databaseConnection import create_connection, findFlightByID, findAllFlights
import json

views = Blueprint('views', __name__)

@views.route('/getFlight', methods=['POST'])
def getFlight():
    try:
        flightID = request.form.get('flightID')  
        conn = create_connection("localhost", "***", "***", "***", "1234")
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

@views.route('/getAllFlights', methods=['GET'])
def getAllFlights():
    try:
        conn = create_connection("localhost", "***", "***", "***", "***")
        flights = findAllFlights(conn)
        conn.close()
        flight_list = []
        for flight in flights:
            flight_list.append({
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
            })
        return jsonify(flight_list)
    except Exception as e:
        print(e)
        return str(e), 500


@views.route('/getTicketsByFlight', methods=['POST'])
def getTicketsByFlight():
    try:
        flightID = request.form.get('flightID')
        conn = create_connection("localhost", "***", "***", "***", "***")
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
        conn = create_connection("localhost", "***", "***", "***", "***")
        pilots = findFlightPilotsByFlightID(conn, flightID)
        conn.close()
        pilot_list = [{"flight_id": pilot[0], "pilot_id": pilot[1]} for pilot in pilots]
        return jsonify(pilot_list)
    except Exception as e:
        print(e)
        return str(e), 500
