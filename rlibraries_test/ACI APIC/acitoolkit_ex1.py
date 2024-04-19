#! /usr/bin/env python
import sys
import acitoolkit.acitoolkit as aci
APIC_URL = 'https://10.10.20.14'
USERNAME = 'admin'
PASSWORD = 'C1sco12345'

# Login to APIC
SESSION = aci.Session(APIC_URL, USERNAME,PASSWORD)
RESP = SESSION.login()
if not RESP.ok:
    print('Could not login to APIC')
    sys.exit() #for what?

ENDPOINTS = aci.Endpoint.get(SESSION)

#build the table collumn names (can do with tabulate, actually will do)
print('{0:19s}{1:14s}{2:10s}{3:8s}{4:17s}{5:10s}'.format("MAC ADDRESS","IP ADDRESS","ENCAP","TENANT","APP PROFILE","EPG"))
print('-'*80)

#populate the table
for EP in ENDPOINTS:
    epg = EP.get_parent()
    app_profile = epg.get_parent()
    tenant = app_profile.get_parent()
    print('{0:19s}{1:14s}{2:10s}{3:8s}{4:17s}{5:10s}'.format(EP.mac,EP.ip,EP.encap,tenant.name,app_profile.name,epg.name))