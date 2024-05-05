class Cars:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.speed = 0
        self.price = 0
    def set_price(price):
        self.price = price
        return self.price
    def showCar(self):
        print(self.name, self.model, self.speed)
    def showPrice(self):
        print(self.price)
        

car1 = Cars("Posche", "Cayenne")
car2 = Cars("Mercedes","ML")
car3 = Cars("BMW","X5")
car4 = Cars("WolsWagen","Touareg")

cars = [car1,car2,car3]

for car in cars:
    car.showCar()