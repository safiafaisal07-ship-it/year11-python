class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.card = 'unknown'
        self.vaccinated = False
    
    def __str__(self):
        payment_status = 'unregistered'
        if len(self.card) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' +str(self.age) + '\nPayment status: ' + payment_status + '\nVaccinated: ' +str(self.vaccinated)
        return my_status
    
p1 = Pet('Bonnie', 'Cat')
p1.card = '2453 3743 3234 2844'

p2 = Pet('Clyde', 'Dog', 7)
p2.card = '5434 2455 7595 2947'

p3 = Pet(category= 'Rabbit', name = 'Ruby', age = 3)
p3.card = '4646 2945 7068 3987'

p4 = Pet(category = 'Snake', name = 'Biscuit', age = 2)
p4.card = '7548 2984 0284 4839'

pets = [p1, p2, p3, p4]
for Pet in pets:
    print(Pet)
    print('') 

vaccinated = {
    "p1": True,
    "p2": False,
    "p3": False,
    "p4": True
}

for pets  in vaccinated:
    print('vaccinated: ')
for Pet in pets:
    print(Pet)
    print('') 
