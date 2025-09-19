class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) ==9:
            my_status = 'Name: ' + self.name +'\nCategory: ' + self.category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status
p1 = Pet('Bonnie', 'Cat')
p1.ccard = '3532 1345 6794 2956'
print(p1)