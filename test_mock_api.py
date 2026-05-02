#Test with mock API
import unittest
from  unittest.mock import patch, Mock
from withoutmock import get_users

#is a relation between TestAPI and TestCase
class TestAPI(unittest.TestCase):
    # This is a test class using unittest framework, inheriting from unittest.TestCase

    @patch('withoutmock.requests.get') # Replace requests.get() 
    #inside module withoutmock with fake object mock_get
    def test_get_users(self, mock_get):
        # Mock response data
        mock_response = Mock()
      
        mock_response.json.return_value = [
            {"id": 1, "name": "vishal"},
            {"id": 2, "name": "Bob"}
        ]
        mock_get.return_value = mock_response
        
        

        # Call the function to test
        result  = get_users()
        print("result: from get request", result)
        

        # Assertions
        self.assertEqual(result, [{ "id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])

