import requests
import json


# GET request to fetch all users
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# print status and formatted JSON
print(response.status_code)
print(json.dumps(response.json(), indent=4))
