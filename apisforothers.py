

from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='1234',
            database='myDB'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")

app = Flask(__name__)

@app.route('/getCabinCrew', methods=['GET'])
def getCabinCrew():
    flightId = request.args.get("flightID")
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT CABIN_CREW_ID
    FROM FLIGHTCABINCREW
    WHERE FLIGHT_ID="{flightId}"
    """)
    data = cursor.fetchall()
    returnList = []
    for crew_id in data:
        cursor.execute(
            f"""
            SELECT *
            FROM CABINCrew
            WHERE ID="{crew_id[0]}"
            """
        )
        crew = cursor.fetchone()
        cursor.execute(
            f"""
            SELECT LANGUAGE
            FROM CABINCREWKNOWNLANGUAGES
            WHERE ID="{crew_id[0]}"
            """
        )
        languages = [lang[0] for lang in cursor.fetchall()]
        returnList.append(
            {"ID": crew[0], "Name": crew[1], "Age": crew[2], "Gender": crew[3], "Nationality": crew[4],
             "Type": crew[5], "Vehicle": crew[6], "Languages": languages})
    cursor.close()
    connection.close()
    return jsonify(returnList)

@app.route('/getPassengerInfo', methods=['GET'])
def getPassengerInfo():
    passengerId = request.args.get("passengerID")
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT *
    FROM PASSANGERINFORMATION
    WHERE ID="{passengerId}"
    """)
    passenger = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify({"ID": passenger[0], "Name": passenger[1], "Age": passenger[2], "Gender": passenger[3], "Nationality": passenger[4]})

@app.route('/getFlightInfo', methods=['GET'])
def getFlightInfo():
    flightId = request.args.get("flightID")
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT *
    FROM FLIGHTINFORMATION
    WHERE ID="{flightId}"
    """)
    flight = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify({"ID": flight[0], "Departure Date": flight[1], "Duration": flight[2], "Distance": flight[3], "Source Country": flight[4], "Source City": flight[5], "Source Airport": flight[6], "Source Airport Code": flight[7], "Vehicle": flight[8], "Shared Flight": flight[9]})

@app.route('/getTickets', methods=['GET'])
def getTickets():
    flightId = request.args.get("flightID")
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT *
    FROM TICKET
    WHERE FLIGHT_ID="{flightId}"
    """)
    tickets = cursor.fetchall()
    result = []
    for ticket in tickets:
        result.append({"Flight ID": ticket[0], "Seat Number": ticket[1], "Type": ticket[2], "Passenger ID": ticket[3]})
    cursor.close()
    connection.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
