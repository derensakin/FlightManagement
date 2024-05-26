#CabinCrewAPI/databaseConnection/__init__.py
import unittest
from unittest.mock import patch, MagicMock
from BackEnd.cabinCrewAPI.databaseConnection import (
    create_connection,
    findCabinCrewsWithID,
    findCabinCrewIDs,
    findCabinCrewLanguagesWithID,
    getMealsWithID,
)

class TestCabinCrewAPI(unittest.TestCase):
    @patch('BackEnd.cabinCrewAPI.databaseConnection.mysql.connector.connect')
    def test_create_connection(self, mock_connect):
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        # Call the function with mock parameters
        connection = create_connection('localhost', 3306, 'myDB', 'root', 'Tonbalikli2003.')

        # Check if the function returned the mocked connection
        self.assertEqual(connection, mock_connection)

    @patch('BackEnd.cabinCrewAPI.databaseConnection.mysql.connector.connect')
    def test_find_cabin_crews_with_id(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchone.return_value = (1, 'John Doe', 25, 'Male', 'US', 'A320', '10 years', 1000)

        # Call the function with mock parameters
        cabin_crew = findCabinCrewsWithID(mock_connection, 123)

        # Check if the function returns the expected cabin crew information
        self.assertEqual(cabin_crew, (1, 'John Doe', 25, 'Male', 'US', 'A320', '10 years', 1000))

    @patch('BackEnd.cabinCrewAPI.databaseConnection.mysql.connector.connect')
    def test_find_cabin_crew_ids(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchall.return_value = [(1), (2), (3)]

        # Call the function with mock parameters
        cabin_crew_ids = findCabinCrewIDs(mock_connection, 'CS101')

        # Check if the function returns the expected list of cabin crew IDs
        self.assertEqual(cabin_crew_ids, [1, 2, 3])

    @patch('BackEnd.cabinCrewAPI.databaseConnection.mysql.connector.connect')
    def test_find_cabin_crew_languages_with_id(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchall.return_value = [('English'), ('French'), ('Spanish')]

        # Call the function with mock parameters
        cabin_crew_languages = findCabinCrewLanguagesWithID(mock_connection, 1)

        # Check if the function returns the expected list of cabin crew languages
        self.assertEqual(cabin_crew_languages, ['English', 'French', 'Spanish'])

    @patch('BackEnd.cabinCrewAPI.databaseConnection.mysql.connector.connect')
    def test_get_meals_with_id(self, mock_create_connection):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_create_connection.return_value = mock_connection

        # Define the mock response for the database query
        mock_cursor.fetchall.return_value = [('Meal1'), ('Meal2'), ('Meal3')]

        # Call the function with mock parameters
        meals = getMealsWithID(mock_connection, 1)

        # Check if the function returns the expected list of meals
        self.assertEqual(meals, ['Meal1', 'Meal2', 'Meal3'])

if __name__ == '__main__':
    unittest.main()
