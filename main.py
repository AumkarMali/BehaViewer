import requests
import json

# Server URL
url = "http://127.0.0.1:5000/get/"

# New user JSON data as a string
new_user_json = json.dumps({
    "name": "Alice Green",
    "provider": "Rogers",
    "Device_Brand": "Samsung Galaxy S21",
    "Device_Plan": "Contract",
    "Gender": "Female",
    "Age": 27
})

# Send the GET request with the JSON data as a URL parameter
response = requests.get(url, params={"data": new_user_json})

# Print the response from the server
if response.status_code == 200:
    print("Server response:", response.json())
else:
    print("Request failed with status code:", response.status_code)
