import requests

def create_user(user_data):
    response =
    requests.post('https://api.example.com/users', json=user_data)
    return response.json()

