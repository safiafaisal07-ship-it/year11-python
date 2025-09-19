import random

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield
    
    def report(self):
        print(self.name+ ':'+ ' Health: '+ str(self.health))

    def random_attack(self):
        attack_power = random.randint(round(self.weapon/2), self.weapon*2)
        return attack_power




you = Fighter('You',100,60,20)
troll = Fighter('Troll',200,30,10)

you.report()
troll.report()
print('You attack the troll')
troll.health -= you.random_attack()
troll.report()



