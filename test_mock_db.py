import unittest
from unittest.mock import Mock
from database_file import get_user_name

class TestGetUserName(unittest.TestCase):
    def test_get_user_name(self):
        # Create a mock database object
        mock_db = Mock()
        # Set up the mock to return a user object with a name attribute
        mock_user = Mock()
        mock_user.name = "Alice"
        mock_db.get_user.return_value = mock_user
        # Call the function to test
        result = get_user_name(mock_db, 1)
        print("result from get_user_name:", result)
        # Assertions
        self.assertEqual(result, "Alice")