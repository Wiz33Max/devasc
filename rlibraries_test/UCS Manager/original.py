#! /usr/bin/env python
from ucsmsdk.ucshandle import UcsHandle
HANDLE = UcsHandle("https://192.168.235.133/nuova", "ucspe","ucspe", port=443,secure=False)

# Login into Cisco UCS Manager
HANDLE.login()

# Retrieve all the compute blades
BLADES = HANDLE.query_classid("ComputeBlade")
print('{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}'.format("DN","SERIAL","ADMIN STATE","MODEL","TOTAL MEMORY"))
print('-'*70)

# Extract DN, serial number, admin state,
# model, and total memory for each blade
for BLADE in BLADES:
    print('{0:23s}{1:8s}{2:12s}{3:14s}{4:6s}'.format(BLADE.dn,BLADE.serial,BLADE.admin_state,BLADE.model,BLADE.total_memory))
HANDLE.logout()