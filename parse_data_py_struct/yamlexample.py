import yaml
from yaml import load, load_all

f = open('parse_data_py_struct\\sample.yaml','r')
documents = load(f, Loader=yaml.FullLoader)
print (documents['people'])
print(documents['people'][2]['LastName'])

