import random


class Mob:
    """Base class"""

    def __init__(self, name, vitality, strength, agility):
        self.name = name
        # Name
        self.vitality = vitality
        # Hit points
        self.strength = strength
        # Physical damage
        # TODO add flat physical reduction for beating armored opponents
        # TODO it'll give a difference between strength and dexterity characters
        self.agility = agility
        # Speed

        self.total_vitality = self.vitality
        # Max health, created when character is created.

    is_alive = True
    # Determines if they can act or be acted on

    def check_life(self):
        # Check if alive

        if self.vitality <= 0:
            print(self.name + " is dead.")
            self.is_alive = False
            # If below, they die.

        """elif self.vitality > 0:
            print(self.name + " lives.")
            # If health is above zero, they live"""

    def attack(self, target):
        # Calculate damage given, reduce target vit, check if alive.

        if target.is_alive and self.is_alive:
            # Check if target and attacker are both alive, else attack is cancelled.

            target_evasion = float(target.agility / self.agility) * 4
            target_evasion += 5
            if target_evasion > 100:
                target_evasion = 100
            # Quotient of agility times 4, + 5, no bigger than 100

            evasion_chance = random.randint(0, 101)
            # Pick a random number.

            # print(str(target_evasion), "%") # Prints evasion chance

            if target_evasion >= evasion_chance:
                print(self.name, "missed", target.name + "!\n")
                return
            # If evasion is higher than random number, end the attack.

            else:
                print(self.name, "attacked", target.name + "!")
                damage_given = self.strength * 2
                print(self.name, "dealt " + str(damage_given), "damage!")
                # Calculate damage dealt

                target.vitality -= damage_given
                # Reduce target vitality
                if target.vitality < 0:
                    target.vitality = 0
                    # If vitality is below 0, assign it 0

                print(target.name, str(target.vitality) + "/" + str(target.total_vitality))
                # Print name, current vit, total vit.

                target.check_life()
                print()
                # Check if alive after reduction

        else:
            return

        # TODO implement hit system to allow str/dex characters to differentiate
        # TODO Implement number of attack hits based on agility
