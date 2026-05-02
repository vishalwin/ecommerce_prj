import requests

def update_user(user_id, data):
    response = requests.put(f"https://api.example.com/users/{user_id}", json=data)
    return response.json()