import requests
from pprint import pprint
url =  "https://sandbox-sdwan-2.cisco.com/dataservice/device"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
Body = {"j_username=devnetuser&j_password=RG!_Yw919_83"}
resp = requests.post (url=url,headers=headers, data =Body, verify = False)
Cookie = resp.headers.get('Set-Cookie')
print (Cookie)
'''
jsi = jsessionid[1]
jsi1 = jsi.split(";")
jsessionid = jsi1[0]

#ookie = "JSESSIONID="+ jsessionid
'''
#Now need to create a session with requests.session(...)
