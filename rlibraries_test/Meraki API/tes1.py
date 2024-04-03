import meraki
from pprint import pprint

API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

dashboard = meraki.DashboardAPI(API_KEY)

organizations = dashboard.organizations.getOrganizations()
## to get the OrgID 575334852396583133
print (type (organizations))
print ("_"*70)

print ("Organization list:\n")
for org in organizations:
    print(f'{org["name"]} : {org['id']}')
    
org_id = 549236

print ("_"*70)
networks = dashboard.organizations.getOrganizationNetworks(org_id)
pprint (networks)
print ("_"*70)
# Network id we will work on : L_646829496481116295

net_id = "L_646829496481105433"

pprint ( dashboard.networks.getNetworkDevices (net_id) )

#clients = dashboard.networks.getNetworkClients(net_id, timespan=60 * 60 * 24 * 14, perPage=1000,total_pages='all')
#print (clients)

#curl https://api.meraki.com/api/v1/organizations -L -H "Bearer: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0"