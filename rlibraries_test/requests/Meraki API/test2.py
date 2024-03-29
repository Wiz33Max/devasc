import meraki
from pprint import pprint

API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
try:
    dashboard = meraki.DashboardAPI (API_KEY)
except Exception as e:
    print ("Error: Invalid API Key - " + e)


org = dashboard.organizations.getOrganizations()
for org_item in org:
    if org_item["name"] == "DevNet Sandbox":
        break

print (org_item['name'])
orgid = org_item['id']

networks = dashboard.organizations.getOrganizationNetworks(orgid)

for network_item in networks:
    break
netid = network_item['id']
print ("The network name is: " + network_item['name'] + " and it's ID is "+ network_item['id'])

devices = dashboard.networks.getNetworkDevices(netid)

for device_item in devices:
    if 'lanIP' in device_item and device_item['lanIP'] == "10.10.10.131":
        break

        
deviceSerial = device_item['serial']

print (deviceSerial)

clients = dashboard.devices.getDeviceClients(deviceSerial, timespan = 2678400)

pprint (clients)
