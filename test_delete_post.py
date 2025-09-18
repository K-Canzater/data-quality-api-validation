import requests
import json

# DELETE request to remove an existing post
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send the DELETE request
response = requests.delete(url)

# Print status and response
print("Status Code:", response.status_code)
print("Response JSON:", response.text)
