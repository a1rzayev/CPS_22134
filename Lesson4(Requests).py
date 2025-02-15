import requests

response = requests.get("https://fake-json-api.mock.beeceptor.com")

if(response.status_code == 200):
    print("person: \n", response.json())
else:
    print("error! send correct request")