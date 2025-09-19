class Pet:
    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
        self.card = 'unknown'
        self.vaccinated = 'false'
p1 = Pet('Bonnie', 'cat', 3)
p2 = Pet('Foxy', 'dog', 4)
print("Pet Name:", p2. name)
print("Pet Category:", p2. category) 
print("Pet Age:",p2. age)
if p1. vaccinated == "true":
    print(p2. name, "is vaccinated")
else:
    print(p2. name, "is not vaccinated")