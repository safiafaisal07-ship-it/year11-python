import random, time
#importing random and time to use in the code
class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print(self.name+ ':'+ 'Health: '+ str(self.health))

    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
        print('Attack power: ', attack_power)
        return attack_power
    
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
                self.health -= damage
                print('Damage: ', damage)
        else:
                print('No Damage')

you = Fighter('You', 100,60,20)
troll = Fighter('Troll',200,30,10)

you.report()
troll.report()

while True:
    print('You attack the troll')
    troll.defend(you.random_attack())
    troll.report()
    time.sleep(2)
    print('')
    if troll.health <= 0:
        print('You win')
        break
    print('The troll attacks you . . .')
    you.defend(troll.random_attack())
    you.report()
    time.sleep(2)
    if you.health <= 0:
        print("The troll wins")
        break
        print('')