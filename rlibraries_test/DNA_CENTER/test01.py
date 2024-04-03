from dnacentersdk import api
dnac = api.DNACenterAPI(username="devnetuser",password="Cisco123!",base_url="https://sandboxdnac.cisco.com:443",version='2.3.5.3',verify=True)
# Find all devices that have 'Switches and Hubs' in their family
devices = dnac.devices.get_device_list(family='Switches and Hubs')
# Print all of demo devices
for device in devices.response:
    print('{:20s}{}'.format(device.hostname, device.upTime))
