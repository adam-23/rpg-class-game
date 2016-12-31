import random


class Mob:
    """Base class, contains all main functions."""

    def __init__(self, name, vitality, strength, agility, defense):
        self.name = name
        # Name
        self.vitality = vitality
        # Hit points
        self.strength = strength
        # Physical damage
        self.agility = agility
        # Speed
        self.defense = defense
        # Flat physical reducer to damage
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

    def single_hit(self, target):
        # Calculate damage given, reduce target vit, check if alive.
        if target.is_alive and self.is_alive:
            # Check if target and attacker are both alive, else attack is cancelled.

            target_evasion = float(target.agility / self.agility) * 4
            target_evasion += 5
            if target_evasion > 100:
                target_evasion = 100
            # Quotient of agility times 4, + 5, no bigger than 100
            # print("target evasion = " + (str(target_evasion)))

            evasion_chance = random.randint(0, 101)
            # print("evasion_chance =", str(evasion_chance))
            # Pick a random number.

            # print(str(target_evasion), "%") # Prints evasion chance

            if target_evasion >= evasion_chance:
                print(self.name, "missed", target.name + "!\n")
                return
            # If evasion is higher than random number, end the attack.

            else:
                print(self.name, "attacked", target.name + "!")
                damage_given = (self.strength * 2) - target.defense
                # Damage is 2 * strength minus target defense

                random_damage_multiplier = float(random.randint(80, 120)/100)
                # print("random damage multiplier =", random_damage_multiplier)
                damage_given = (float(random_damage_multiplier * damage_given))
                # print("un-rounded float damage = ", damage_given)
                # Multiply by random number between .8 and 1.2

                damage_given = int(round(damage_given))
                # Round the damage after randomizing
                if damage_given == 0:
                    damage_given = 1
                    # Minimum attack damage is always 1

                print(self.name, "dealt " + str(damage_given), "damage!")
                # Print damage

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


    def attack(self, target):
        hits_number = float(self.agility / 8)
        # Hits are agility / 8

        hits_number = int(round(hits_number))
        # Round hits to a float

        if hits_number < 1:
            hits_number = 1
            # Always attack at least once

        for i in range(0, hits_number):
            self.single_hit(target)
            # Call the single hit function repeatedly