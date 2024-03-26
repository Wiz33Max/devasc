import json
from pprint import pprint
filename = "C:/py_files/interface.json"

with open(filename) as file:
    data = json.load(file)

print(type(data))
pprint(data)

data["interface"]["description"] = "***to internet***"

with open(filename, "w") as file:
    json.dump(data, file, indent = 4)


with open(filename) as file:
    data = json.load(file)

print(type(data))
pprint(data)