import requests

def get_users():
    response = requests.get("https://api.example.com/users")
    return response.json()




# problem
# needs internet connection
# api may fail
# slow


