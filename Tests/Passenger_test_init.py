import unittest
from unittest.mock import MagicMock, patch
from BackEnd.Passenger_API.views import views  # Import your Flask views here
from BackEnd.Passenger_API.createApplication import create_app

class TestPassengerViews(unittest.TestCase):
    
    @patch('BackEnd.Passenger_API.databaseConnection.mysql.connector.connect')
    @patch('BackEnd.Passenger_API.databaseConnection.findPassengersByFlightID')
    def test_getPassenger(self, mock_findPassengersByFlightID, mock_create_connection):
        # Setup
        mock_conn = MagicMock()
        mock_create_connection.return_value = mock_conn
        mock_findPassengersByFlightID.return_value = ['123', '456']
        expected_output = '{"passengers": ["123", "456"]}'

        # Test
        with views.test_client() as client:
            response = client.post('/getPassenger', data={'flight_id': 'ABC123'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), expected_output)

    @patch('BackEnd.Passenger_API.databaseConnection.create_connection')
    @patch('BackEnd.Passenger_API.databaseConnection.change_seats')
    def test_changeSeats(self, mock_change_seats, mock_create_connection):
        # Setup
        mock_conn = MagicMock()
        mock_create_connection.return_value = mock_conn
        mock_change_seats.return_value = True
        expected_output = '{"status": "success"}'

        # Test
        with views.test_client() as client:
            response = client.post('/changeSeats', data={'flight_id': 'ABC123', 'passenger_id1': '123', 'passenger_id2': '456'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), expected_output)

if __name__ == '__main__':
    unittest.main()
