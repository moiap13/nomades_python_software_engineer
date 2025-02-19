import requests
import json

url = "http://127.0.0.1:8081/users"

payload = json.dumps({
  "email": "moiap13@gmail.com",
  "username": "moiap13",
  "password": "1234567890",
  "lastname": "Pisanello",
  "firstname": "Antonio"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
print(response.json())