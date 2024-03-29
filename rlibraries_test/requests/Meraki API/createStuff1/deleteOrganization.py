import meraki
from pprint import pprint

API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

dashboard = meraki.DashboardAPI (API_KEY)

#Multiple runs overwrite create new ones FFS
##responce = dashboard.organizations.createOrganization ("Wiz3Max's Organization")

##pprint (responce)
#"id": "575334852396585245", 
#update info

#pprint (dashboard.organizations.getOrganization("575334852396585245"))

#delete
#pprint (dashboard.organizations.deleteOrganization("575334852396585245"))

#try:
#    pprint (dashboard.organizations.getOrganization("575334852396585245"))
#except Exception as e :
#    print (e)

#______________________________________________________
#delete multiple ones

orgs = dashboard.organizations.getOrganizations ()

ids = []

for org in orgs:
    if org['name'] == "Wiz3Max's Organization":
        ids.append ({'name': org['name'], 'id': org['id']})

pprint (ids)

id={}

for id in ids:
    pprint (dashboard.organizations.deleteOrganization(id['id']))
