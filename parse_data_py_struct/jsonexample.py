import json

jsonstr = """{"people":[{"Id":"1","FirstName":"Benjamin","LastName":"Finkel",
    "Email":"ben.finkel@cbtnuggets.com"},{"Id":"2","FirstName":"Jane","LastName":"Doe",
    "Email":"jane.doe@cbtnuggets.com"},{"Id":"3","FirstName":"Pat","LastName":"Smith",
    "Email":"pat.smith@cbtnuggets.com"}]}"""

# Deserialize a STRING to python obj. load[s] (s like string)
jsonobj = json.loads(jsonstr)

print(jsonobj['people'][1])
print("\n")

jsonobj = json.load(open('./sample.json'))

print(jsonobj['people'])


