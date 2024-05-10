import requests
import json

url = "https://reqres.in/api/users"

payload = json.dumps({
  "id": 7,
  "email": "Ignacio.ramos@reqres.in",
  "first_name": "Ignacio",
  "Trabajo": "Profesor",
  "avatar": "https://reqres.in/img/faces/6-image.jpg"
})
headers = {
  'Content-Type': 'application/json'
}

#crear nuevo usuario
response = requests.request("POST", url, headers=headers, data=payload)
created_user = json.loads(response.text)

print(response)
print(created_user)