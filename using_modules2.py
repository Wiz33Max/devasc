from class_test import Circle
#added the following definition into the current namespace
#can add all like this "from class_test import *"


#now usable withouy prependint the module name to the methode
circle1 = Circle (10)

print (circle1.circumference())
