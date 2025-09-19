class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0
    
    def have_birthday(self):
        self.age += 1
    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'
        my_status = 'Name: ' + self.name +'\nCategory :' + self.category + '\nAge: ' +str(self.age) +'\nPayment_status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status
            
