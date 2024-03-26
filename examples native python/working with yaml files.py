import yaml
from pprint import pprint
filename = "C:/py_files/interface.yaml"
def parse_yaml(filename):
    """Load a YAML file into a Python dictionary."""
    try:
        with open(filename, 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    except Exception as e:
        print(e)

def unparse_yaml_to_file (filename):
    """Unparse a Python dictionary into a YAML file."""
    try:
        with open(filename, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except Exception as e:
        print(e)

data = parse_yaml (filename)
print("\n" + "_"* 50 + "\n")
print (type(data))
pprint (data)

data['interface']['description'] = "Wize33Max's interface"

print("\n" + "_"* 50 + "\n")
print (yaml.dump(data))
unparse_yaml_to_file (filename)
