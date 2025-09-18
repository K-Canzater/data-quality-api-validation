import requests
import json

# POST request to create a new post
url = "https://jsonplaceholder.typicode.com/posts"

# Data we want to send
payload = {
    "title": "API Testing Demo Post",
    "body": "Demonstrating POST request using Python for API testing.",
    "userId": 1,
}

# Send the POST request
response = requests.post(url, json=payload)

# Print status and formatted JSON response
print("Status Code:", response.status_code)
print("Response JSON:", json.dumps(response.json(), indent=4))
