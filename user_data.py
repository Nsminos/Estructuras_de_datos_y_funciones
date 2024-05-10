import requests
import json

def requests_get(url):
    return json.loads(requests.get(url).text)

if __name__=='__main__':
    response1 = requests_get('https://reqres.in/api/users')
    response2 = requests_get('https://reqres.in/api/users?page=2')
    len(response1)
    len(response2)
    #Obtener toda la información
    print(response1,response2)