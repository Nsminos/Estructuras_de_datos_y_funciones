import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

#payload = ""
#headers = {}

#response = requests.request("GET", url, headers=headers, data=payload)
def request_json(url):
    return json.loads(requests.get(url).text)
data = request_json('https://jsonplaceholder.typicode.com/photos')
#print(response.text)
