class Car:
    def __init__(self,make,model,year,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    def __str__(self):
        c1 = Car('Mazda','6',2005)
        cars = [c1]
for car in cars:
    print(car)