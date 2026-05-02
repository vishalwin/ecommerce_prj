import pytest
from unittest.mock import Mock
from database_file import get_user_name 

@pytest.fixture
def mock_db():
    # Create a mock database object
    mock_db = Mock()
    mock_db.get_user.return_value ={
        "id": 101,
        "name": "Antonio Mano" 
        
    }
    return mock_db

def test_get_user_name(mock_db,user_id=101):
    result = mock_db.get_user(user_id)
    print("result from get_user_name:", result)
    assert result["name"] == "Antonio Mano" 