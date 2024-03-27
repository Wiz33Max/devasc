import requests

url = "https://postman-echo.com/post"

headers ={}
data = {"test":"fuck yesh im a DEVNET"}

responce = requests.request ("POST", url, headers=headers, data=data)

print (responce.text)
