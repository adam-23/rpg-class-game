import random


class Mob:
    """Base class, contains all main functions."""

    def __init__(self, name, vitality, strength, agility, defense, intelligence, spirit, magic_points):
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
        self.intelligence = intelligence
        # Intelligence based magic defense and attack
        self.spirit = spirit
        # Spirit based magic defense and attack
        self.magic_points = magic_points

        self.total_vitality = self.vitality
        # Max health, created when character is created.
        self.total_magic_points = self.magic_points

    is_alive = True
    # Determines if they can act or be acted on

    def check_life(self):
        # Check if alive

        if self.vitality <= 0:
            print(self.name + " is dead.")
            self.is_alive = False
            # If below, they die.

        """
        elif self.vitality > 0:
            print(self.name + " lives.")
            # If health is above zero, they live
        """

    def attack(self, target):

        """
        1. Check life
        2. Hit or miss
        3. Determine number of hits
        4. Determine damage individually per hit
        5. Deal total damage from hits
        6. Print all information
        7. Close and return all info
        """
        total_damage_given = 0

        if target.is_alive and self.is_alive:
            # Check if target and attacker are both alive, else attack is cancelled.

            target_evasion = float(target.agility / self.agility) * 4
            target_evasion += 5
            if target_evasion > 50:
                target_evasion = 50
            # Quotient of agility times 4, + 5, no bigger than 50

            evasion_chance = random.randint(0, 101)
            # Pick a random number.

            if target_evasion >= evasion_chance:
                print(self.name, "missed", target.name + "!\n")
                return
                # If evasion is higher than random number, end the attack.

            hits_number = float(self.agility / 8)
            # Hits are agility / 8

            hits_number = int(round(hits_number))
            # Round hits to a whole number

            if hits_number < 1:
                hits_number = 1
                # Always attack at least once

            for i in range(0, hits_number):

                damage_given = (self.strength * 2) - target.defense
                # Damage is 2 * strength minus target defense

                random_damage_multiplier = float(random.randint(80, 120) / 100)
                # print("random damage multiplier =", random_damage_multiplier)

                damage_given = (float(random_damage_multiplier * damage_given))
                # print("un-rounded float damage = ", damage_given)
                # Multiply by random number between .8 and 1.2

                damage_given = int(round(damage_given))
                # Round the damage after randomizing
                if damage_given == 0:
                    damage_given = 1
                    # Minimum attack damage is always 1
                # Check if alive after reduction
                # Print damage
                total_damage_given += damage_given

            target.vitality -= total_damage_given
            # Reduce target vitality
            if target.vitality < 0:
                target.vitality = 0
                # If vitality is below 0, assign it 0

            print(self.name, "attacked", target.name + "!")
            print(self.name + " dealt " + str(hits_number) + " hits!")
            print(self.name, "dealt " + str(total_damage_given), "damage!")
            print(target.name, "HP :", str(target.vitality) + "/" + str(target.total_vitality))
            # Print target, hits, damage, target health

            target.check_life()
            # Check if target is dead. If so, mark them as such.
            print()
        else:
            return

    backRow = False
    # Can't be attacked with melee commands until front rows are killed

    rangedAttacker = False
    # Melee or ranged damage

    # TODO MP regen after every battle, action
    # TODO Row system
