import unittest
from unittest.mock import patch, Mock
from mock_put import update_user 

class TestUpdateUser(unittest.TestCase):
    @patch('test_mock_put.requests.put')
    def test_update_user(self, mock_put):
        # Mock response data
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "name": "Alice Updated"}
        mock_put.return_value = mock_response
        
        # Call the function to test
        result = update_user(1, {"name": "Alice Updated"})
        print("result from put request:", result)
        
        # Assertions
        self.assertEqual(result, {"id": 1, "name": "Alice Updated"})  
