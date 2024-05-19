import xmltodict
from pprint import pprint

#Get the XML file data
f = open('parse_data_py_struct\\sample.xml','r')
#Prase the XML file into an 'OrderedDict'
print ("\nUsable dictionary object:\n")
xml = xmltodict.parse(f.read())
pprint (xml)
for e in xml["People"]["Person"]:
    print(f"ID - {e['@Id']}\nName - {e['FirstName']} {e['LastName']}\nEmail - {e['Email']}")
    # print(e['@Id'])
    print (f"")
    print (e.pop('@Id'))