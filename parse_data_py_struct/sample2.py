from lxml import etree as ET

#Get the XML file data
f = open('parse_data_py_struct\\sample.xml','r')

#Parse the data into an ElementTree object
xml = ET.parse(f)

#Get the 'root' Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #Print the stringified version of the element
    print(ET.tostring(e))
    print("")

    #Print the 'Id' attribute of the Element object
    print(f"Id is {e.get("Id")}")