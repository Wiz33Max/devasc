import requests
from pprint import pprint
import requests
#get organizations
##url = "https://api.meraki.com/api/v1/organizations/"



#get organization networks
#url = "https://api.meraki.com/api/v1/organizations/549236/networks"


#get organization devices
##url = "https://api.meraki.com/api/v1/organizations/865776/devices"


#Get network devices Network id L_646829496481105433
##url = "https://api.meraki.com/api/v1/networks/L_646829496481105433/devices"

#get network clients
##url = "https://api.meraki.com/api/v1/networks/L_646829496481105433/clients"

#get device client
url = "https://api.meraki.com/api/v1/devices/Q2QN-9J8L-SLPD/clients"



payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

response = requests.request("GET", url, headers=headers, data=payload)

pprint(response.text)
