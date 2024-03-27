from requests import get as get

url = "https://postman-echo.com/get"
data = {}
headers = {}

responce = get(url = url, headers = headers, data = data)

print (responce.text)