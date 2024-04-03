from dnacentersdk import api

# Create a DNACenterAPI connection object;
# it uses DNA Center sandbox URL, username and password, with DNA Center API version 2.3.5.3.
# and requests to verify the server's TLS certificate with verify=True.
dnac = api.DNACenterAPI(username="devnetuser",password="Cisco123!",base_url="https://sandboxdnac.cisco.com:443",version='2.3.5.3',verify=True)

# Find all devices that have 'Switches and Hubs' in their family
devices = dnac.devices.get_device_list(family='Switches and Hubs')

# Print all of demo devices
for device in devices.response:
    print('{:20s}{}'.format(device.hostname, device.upTime))

# Find all tags
all_tags = dnac.tag.get_tag(sort_by='name', order='des')
demo_tags = [tag for tag in all_tags.response if 'Demo' in tag.name ]

#  Delete all of the demo tags
for tag in demo_tags:
    dnac.tag.delete_tag(tag.id)

# Create a new demo tag
demo_tag = dnac.tag.create_tag(name='dna Demo')
task_demo_tag = dnac.task.get_task_by_id(task_id=demo_tag.response.taskId)

if not task_demo_tag.response.isError:
    # Retrieve created tag
    created_tag = dnac.tag.get_tag(name='dna Demo')

    # Update tag
    update_tag = dnac.tag.update_tag(id=created_tag.response[0].id,
                                     name='Updated ' + created_tag.response[0].name,
                                     description='DNA demo tag')

    print(dnac.task.get_task_by_id(task_id=update_tag.response.taskId).response.progress)

    # Retrieved updated
    updated_tag = dnac.tag.get_tag(name='Updated dna Demo')
    print(updated_tag)
else:
    # Get task error details
    print('Unfortunately ', task_demo_tag.response.progress)
    print('Reason: ', task_demo_tag.response.failureReason)

# Advance usage example using Custom Caller functions
# Define the get_global_credentials and create_netconf_credentials functions
# under the custom_caller wrapper.
# Call them with:
#     dnac.custom_caller.get_global_credentials('NETCONF')
#     dnac.custom_caller.create_netconf_credentials('65533')
def setup_custom():
    dnac.custom_caller.add_api('get_global_credentials',
                            lambda credential_type:
                                dnac.custom_caller.call_api(
                                    'GET',
                                    '/dna/intent/api/v1/global-credential',
                                    params={
                                        'credentialSubType': credential_type
                                    }).response
                            )
    dnac.custom_caller.add_api('create_netconf_credentials',
                            lambda port:
                                dnac.custom_caller.call_api(
                                    'POST',
                                    '/dna/intent/api/v1/global-credential/netconf',
                                    json=[{
                                        "netconfPort": port
                                    }])
                            )

# Add the custom API calls to the connection object under the custom_caller wrapper
setup_custom()
# Call the newly added functions
dnac.custom_caller.create_netconf_credentials('65533')
print(dnac.custom_caller.get_global_credentials('NETCONF'))