class Pet:
    def __init__(self, name, category, breed=None, age=0):
        self._name = name
        self.__category = category  
        self.__breed = breed  
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False

    def have_birthday(self):
        self.age += 1

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = (
            f"Name: {self._name}\nCategory: {self.__category}\nBreed: {self.__breed}\n"
            f"Age: {self.age}\nPayment status: {payment_status}\nVaccinated: {self.vaccinated}"
        )
        return my_status

    def get_category(self):  
        return self.__category

    def get_breed(self): 
        return self.__breed


p1 = Pet(name="Bonnie", category="Cat", breed="Siamese", age=10)
print(p1)

try:
    p1.__category = "Dog"
except AttributeError as e:
    print("Modification of category failed:", e)

try:
    p1.__breed = "Bulldog"
except AttributeError as e:
    print("Modification of breed failed:", e)

print("Category:", p1.get_category())
print("Breed:", p1.get_breed())   