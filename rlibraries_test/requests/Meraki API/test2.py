import meraki
from pprint import pprint

API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

dashboard = meraki.DashboardAPI (API_KEY)

org = dashboard.organizations.getOrganizations()
for org_item in org:
    if org_item["name"] == "DevNet Sandbox":
        break

print (org_item['name'])
orgid = org_item['id']

networks = dashboard.organizations.getOrganizationNetworks()