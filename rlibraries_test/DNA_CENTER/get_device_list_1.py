from dnac_config import DNAC_USER, DNAC_PASSWORD
from requests.auth import HTTPBasicAuth
import requests
from pprint import pprint
def get_token():
    url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
    token_str = requests.post(url = url, auth = HTTPBasicAuth(username=DNAC_USER, password=DNAC_PASSWORD), verify = False).json()
    return token_str['Token']

def get_devices():
    url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
    token = get_token()
    headers = {"x-auth-token":token}
    data = {}
    resp = requests.get(url=url, headers=headers, data= data, verify = False).json()
    return resp['response']

def printdevicelist():
    i = 1
    devices_list = get_devices()
    for device in devices_list:
        print ("Device No "+str(i))
        print (device['hostname']+" "+ device['family'] + " "+ device['managementIpAddress']) 
        print ("\n")
printdevicelist()
'''
try:
    token = (get_token())
except Exception as e:
    print (e)
print (tkn)
'''