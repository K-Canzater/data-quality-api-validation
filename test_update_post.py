import requests
import json

# PUT request to update an existing post
url = "https://jsonplaceholder.typicode.com/posts/1"

# Data we want to update
payload = {
    "id": 1,
    "title": "API Testing Demo Post (Updated)",
    "body": "Demonstrating PUT request using Python for API testing.",
    "userId": 1,
}

# Send the PUT request
response = requests.put(url, json=payload)

# Print status and formatted JSON response
print("Status Code:", response.status_code)
print("Response JSON:", json.dumps(response.json(), indent=4))
