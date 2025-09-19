name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
card = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
#17 Park Street

owner_name = 'Alex Nguyen'
account_balance = 129.95

print(name)
print(animal_category)
age += 1
print(age)
print(billing_address.replace("Drive", "Street"))
vaccinated = False
new_card = input('Do u want to change your card number?')
if new_card == 'yes':
    input('new card number:')
    print(new_card)
print(card)
print(vaccinated)
print(owner_name.replace("Nguyen", "Jones"))
print(account_balance - 25)