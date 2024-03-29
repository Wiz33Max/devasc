import meraki

API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

responce = meraki.Organizations.getOrganization(API_KEY)

print (responce)