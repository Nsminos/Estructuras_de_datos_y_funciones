import requests


url = "https://reqres.in/api/users/6"


# Eliminar un usuario
response = requests.request("DELETE", url)
delete = response


print(delete)