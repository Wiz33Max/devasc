import xmltodict
from pprint import pprint

filename = "C:/py_files/interface_yang.xml"

with open (filename, "r") as file:
    data = xmltodict.parse(file.read())

print(type(data))  
pprint(data)

print("\n" + "_"* 50 + "\n")

print (xmltodict.unparse(data, pretty = True))
data["interface"]["ipv4"]["address"]["ip"] = "10.10.0.1"

with open (filename, "w") as file:
    file.write(xmltodict.unparse(data, pretty=True))
