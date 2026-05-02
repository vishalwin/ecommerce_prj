import unittest
from unittest.mock import patch, Mock
from mock_post import create_user
class TestCreateUser(unittest.TestCase):
    @patch('mock_post.requests.post')    
    def test_create_user(self, mock_post):
        # Mock response data
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "name": "Alice"}
        mock_post.return_value = mock_response
        
        # Call the function to test
        result = create_user({"name": "Alice"})
        print("result from post request:", result)
        
        # Assertions
        self.assertEqual(result, {"id": 1, "name": "Alice"})