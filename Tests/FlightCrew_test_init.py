# test_flight_crew_api.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from BackEnd.flightCrewAPI_1_01.views import views  # Adjust the import according to your project structure

class TestFlightCrewAPI(unittest.TestCase):
    @patch('BackEnd.flightCrewAPI_1_01.databaseConnection.create_connection')
    def test_getFlightCrew(self, mock_create_connection):
        # Set up the mock database connection and cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_create_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Mock the database responses
        mock_cursor.fetchall.side_effect = [
            [("Pilot1",)],  # Result of the first query
            [("English",), ("French",)],  # Result of the third query
        ]
        mock_cursor.fetchone.return_value = ("Pilot1", "John Doe", 35, "Male", "USA", "Boeing 747", 10, 10000)

        # Set up the Flask app and test client
        app = Flask(__name__)
        app.register_blueprint(views, url_prefix='/api')

        with app.test_client() as client:
            # Mock the request data
            data = {'flightID': 'CS1031'}

            # Call the function
            response = client.post('/api/getFlightCrew', data=data)
            response_data = json.loads(response.data)

            # Verify the response
            expected_response = [{
                "ID": "Pilot1",
                "Name": "John Doe",
                "Age": 35,
                "Gender": "Male",
                "Nationality": "USA",
                "Vehicle": "Boeing 747",
                "Seniority": 10,
                "Max_Distance": 10000,
                "Languages": ["English", "French"]
            }]
            self.assertEqual(response_data, expected_response)

            # Verify the database interactions
            mock_cursor.execute.assert_any_call(
                """
                SELECT PILOT_ID
                FROM FLIGHTPILOT
                WHERE FLIGHT_ID="CS1031"
                """
            )
            mock_cursor.execute.assert_any_call(
                """
                SELECT *
                FROM FLIGHTCREW
                WHERE ID="Pilot1"
                """
            )
            mock_cursor.execute.assert_any_call(
                """
                SELECT LANGUAGE
                FROM FLIGHTCREWKNOWNLANGUAGES
                WHERE ID="Pilot1"
                """
            )
            mock_cursor.close.assert_called_once()
            mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
