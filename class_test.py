class Circle:
    radius = 0
    otherVars = "whatever"
    def __init__(self,r):
        self.radius = r

    def circumference(self):
        return (self.radius * 2 * 3.14)
    
circle1 = Circle (10)

print (circle1.circumference())

#OOP supports DRY and KISS programming principles

