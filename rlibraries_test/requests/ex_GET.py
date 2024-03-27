import requests

url = "https://postman-echo.com/get"

data = {"test":"123"}
#apparently having params instead if data raises an exception, no need to bother
headers = {}

response = requests.request("GET", url, headers=headers, data=data)

print(response.text)
