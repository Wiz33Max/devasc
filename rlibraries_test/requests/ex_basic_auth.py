import requests

url = "https://postman-echo.com/basic-auth"

data = {}
headers = {"authorization":"Basic cG9zdG1hbjpwYXNzd29yZA=="}

responce = requests.get (url = url, data=data, headers=headers)

print (responce.text)
