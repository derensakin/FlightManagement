#get_passenger_api/app/main.py
import unittest
from unittest.mock import patch, MagicMock
from get_passenger_api import (
    create_connection,
    assign_seat,
    get_passengers,
)

class TestPassengerAPI(unittest.TestCase):
    @patch('myapp.mysql.connector.connect')
    def test_create_connection(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        # Call the function with mock parameters
        connection = create_connection()

        # Check if the function returned the mocked connection
        self.assertEqual(connection, mock_connection)

    @patch('myapp.create_connection')
    def test_assign_seat_infant(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database queries
        mock_cursor.fetchone.side_effect = [(2, 'parent_seat')]

        # Call the function with mock parameters
        seat_number = assign_seat('infant_id', 'flight_id')

        # Check if the function assigns the parent's seat for infants
        self.assertEqual(seat_number, 'parent_seat')

    @patch('myapp.create_connection')
    def test_assign_seat_regular(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database queries
        mock_cursor.fetchone.side_effect = [None, ('available_seat',)]

        # Call the function with mock parameters
        seat_number = assign_seat('regular_passenger_id', 'flight_id')

        # Check if the function assigns an available seat for regular passengers
        self.assertEqual(seat_number, 'available_seat')

    @patch('myapp.create_connection')
    def test_get_passengers(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchall.return_value = [
            ('passenger1_id', 'Passenger 1', 25, 'Male', 'US', 'Business', '1A'),
            ('passenger2_id', 'Passenger 2', 30, 'Female', 'UK', 'Economy', '10B'),
        ]

        # Call the function with mock parameters
        passengers = get_passengers()

        # Check if the function returns the expected list of passengers
        self.assertEqual(passengers, [
            {"ID": 'passenger1_id', "Name": 'Passenger 1', "Age": 25, "Gender": 'Male',
             "Nationality": 'US', "Seat Type": 'Business', "Seat Number": '1A'},
            {"ID": 'passenger2_id', "Name": 'Passenger 2', "Age": 30, "Gender": 'Female',
             "Nationality": 'UK', "Seat Type": 'Economy', "Seat Number": '10B'},
        ])

if __name__ == '__main__':
    unittest.main()
