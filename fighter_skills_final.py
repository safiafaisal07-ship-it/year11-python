import random

class Fighter:
    """Represents a basic fighter character with health, weapon power, and shield defense."""
    def __init__(self, name, health, weapon, shield):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.shield = shield
        # checks the health of the player, power of the weapon and the shield stats

    def is_dead(self):
        """Checks if the fighter has been defeated."""
        return self.health <= 0

    def report(self):
        """Displays the fighter’s current health."""
        print(f"{self.name}: Health = {self.health}")

    def random_attack(self):
        """Performs an attack with randomized damage based on weapon strength."""
        return random.randint(self.weapon // 2, self.weapon * 2)

    def skill_attack(self):
        """Skill attack without a timer, using a fixed multiplier."""
        multiplier = 2  # Set a static multiplier instead of using timing-based variation
        base = self.random_attack()
        total = base * multiplier
        print(f"Skill Attack: {base} x {multiplier} = {total}")
        return total

    def defend(self, damage):
        """Calculates reduced damage based on shield protection."""
        reduced = max(0, damage - self.shield)
        self.health -= reduced
        print(f"{self.name} takes {reduced} damage! Shield blocked {damage - reduced}")

class Wizard(Fighter):
    """A special fighter class with magic abilities that enhance attacks."""
    def __init__(self, name, health, weapon, shield, magic):
        super().__init__(name, health, weapon, shield)
        self.magic = magic  # Additional magic attack power

    def random_attack(self):
        """Performs an attack with magic-enhanced damage."""
        base_attack = super().random_attack()
        return base_attack + self.magic

# Teams Setup, pak has four allies so does the enemies:-
team_pak = [
    Fighter("Pak", 100, 25, 10),
    Fighter("China", 90, 20, 20),
    Wizard("Turkey", 80, 30, 10, 15),  # Wizard added
    Fighter("Saudi Arabia", 110, 35, 5)
]
#team bangla
enemies = [
    Fighter("Japan", 70, 25, 5),
    Fighter("US", 100, 40, 10),
    Fighter("Russia", 120, 20, 30),
    Wizard("Bangla", 150, 45, 15, 20)  # Final enemy, enhanced with magic
]

print("STORY: Indiana has been kidnapped by Bangla! Pak and his allies set out to defeat Bangla's team and save her.\n")

for i, enemy in enumerate(enemies):
    print(f"Enemy Appears: {enemy.name}\n")
    player = team_pak[i % len(team_pak)]
    print(f"You are {player.name}! Prepare to fight {enemy.name}.\n")

    while not player.is_dead() and not enemy.is_dead():
        print("\nYour Turn!")
        player.report()
        enemy.report()
        move = input("Choose your attack (1 - Random, 2 - Skill): ")
        if move == '2':
            dmg = player.skill_attack()
        else:
            dmg = player.random_attack()
        print(f"{player.name} attacks for {dmg}")
        enemy.defend(dmg)

        if enemy.is_dead():
            print(f"{enemy.name} is defeated!\n")
            if enemy.name == "Bangla":
                print("Final Battle Won! Indiana is rescued. Pak wins!")
            else:
                print(f"Cutscene: {enemy.name} falls. On to the next enemy...\n")
            break

        print(f"{enemy.name}'s Turn!")
        enemy_dmg = enemy.random_attack()
        print(f"{enemy.name} attacks for {enemy_dmg}")
        player.defend(enemy_dmg)

        if player.is_dead():
            print(f"{player.name} is defeated! Bangla's team wins.")
            exit()

print("\nTHE END")