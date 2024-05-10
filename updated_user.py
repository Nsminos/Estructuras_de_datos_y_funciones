import requests
import json

url = "https://reqres.in/api/users/2"


payload = json.dumps({
  "id": 2,
  "email": "morpheus.weaver@reqres.in",
  "first_name": "Morpheus",
  "Residence": "Zion",
  "avatar": "https://reqres.in/img/faces/2-image.jpg"
})
headers = {
  'Content-Type': 'application/json'
}

#Modificar un usuario
response = requests.request("PUT", url, headers=headers, data=payload)
updated_user = json.loads(response.text)

print(response)
print(updated_user)