#---begin Python ---
class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

# Instantiating objects from the Car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")

car1.start()  # Output: Toyota Camry is starting.
car2.stop()   # Output: Honda Civic is stopping.
#--- end python ---
# Creates another object car with the make, model, year and colour
car3 = Car("Ford", "Mustang", 2021, "Black")

car3.start()  
#prints out the car with the car is starting
