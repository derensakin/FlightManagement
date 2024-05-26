#Flightinfo_api/DBconnection.py
import unittest
from unittest.mock import patch, MagicMock
from BackEnd import (
    create_connection,
    findFlightByID,
    findFlightsAdvanced,
    findTicketsByFlightID,
    findFlightPilotsByFlightID,
)

class TestFlightInfoAPI(unittest.TestCase):
    @patch('myapp.mysql.connector.connect')
    def test_create_connection(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        # Call the function with mock parameters
        connection = create_connection('localhost', 3306, 'myDB', 'root', '1234')

        # Check if the function returned the mocked connection
        self.assertEqual(connection, mock_connection)

    @patch('myapp.create_connection')
    def test_find_flight_by_id(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchone.return_value = (1, 'Flight 1', '2024-05-30', '10:00:00', 'NYC', 'LAX', '123ABC')

        # Call the function with mock parameters
        flight_info = findFlightByID(mock_connection, '123')

        # Check if the function returns the expected flight information
        self.assertEqual(flight_info, (1, 'Flight 1', '2024-05-30', '10:00:00', 'NYC', 'LAX', '123ABC'))

    @patch('myapp.create_connection')
    def test_find_flights_advanced(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchall.return_value = [(1, 'Flight 1'), (2, 'Flight 2')]

        # Call the function with mock parameters
        filters = {'destination': 'LAX'}
        flights = findFlightsAdvanced(mock_connection, filters)

        # Check if the function returns the expected list of flights
        self.assertEqual(flights, [(1, 'Flight 1'), (2, 'Flight 2')])

    @patch('myapp.create_connection')
    def test_find_tickets_by_flight_id(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchall.return_value = [('Ticket1', 'John Doe'), ('Ticket2', 'Jane Smith')]

        # Call the function with mock parameters
        tickets = findTicketsByFlightID(mock_connection, '123')

        # Check if the function returns the expected list of tickets
        self.assertEqual(tickets, [('Ticket1', 'John Doe'), ('Ticket2', 'Jane Smith')])

    @patch('myapp.create_connection')
    def test_find_flight_pilots_by_flight_id(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchall.return_value = [('Pilot1', 'John Doe'), ('Pilot2', 'Jane Smith')]

        # Call the function with mock parameters
        pilots = findFlightPilotsByFlightID(mock_connection, '123')

        # Check if the function returns the expected list of pilots
        self.assertEqual(pilots, [('Pilot1', 'John Doe'), ('Pilot2', 'Jane Smith')])

if __name__ == '__main__':
    unittest.main()
