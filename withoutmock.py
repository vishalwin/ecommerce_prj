import requests

def get_users():
    response = requests.get("https://api.example.com/users")
    return response.json()


def update_user(user_id, data):
    response = requests.put(f"https://api.example.com/users/{user_id}", json=data)
    return response.json()

# problem
# needs internet connection
# api may fail
# slow


