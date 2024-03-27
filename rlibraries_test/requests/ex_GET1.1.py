from requests import request as request

url = "https://postman-echo.com/get"
data = {}
headers={}

responce = request ("GET", url, data=data,headers=headers)

print (responce.text)