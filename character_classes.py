from mob_class import *


class Player(Mob):
    """Base human class"""


# Warrior Classes
class Fighter(Player):
    None


class Hoplite(Fighter):

    """Base spear-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=55, strength=12, agility=5, defense=8,
                         intelligence=4, spirit=4, magic_points=2)


class Soldier(Fighter):
    """Base sword-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=50, strength=12, agility=7, defense=8,
                         intelligence=4, spirit=5, magic_points=4)


class FistFighter(Fighter):
    """Base fist-fighting class"""
    def __init__(self, name):
        super().__init__(name, vitality=45, strength=12, agility=11, defense=8,
                         intelligence=4, spirit=4, magic_points=3)


# Rogue classes (base)
class Thief(Player):
    None


class Scout(Thief):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=45, strength=8, agility=15, defense=7,
                         intelligence=4, spirit=5, magic_points=4)


class Archer(Thief):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=35, strength=7, agility=13, defense=7,
                         intelligence=5, spirit=4, magic_points=4)
        # TODO add row system
        # TODO make Archer unaffected by range in rows


class Rogue(Thief):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=40, strength=9, agility=13, defense=7,
                         intelligence=4, spirit=4, magic_points=2)


# Caster classes (base)
class Caster(Player):
    def pulse(self, target):

        if target.is_alive and self.is_alive and self.magic_points > 1:
            self.magic_points -= 1
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

            total_damage_given = 0

            damage_given = (self.intelligence * self.spirit) / ((target.intelligence + target.spirit) / 4)

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

            print(self.name, "cast Pulse on", target.name + "!")
            print(self.name, "MP :", str(self.magic_points) + "/" + str(self.total_magic_points))
            print(self.name, "dealt " + str(total_damage_given), "damage!")
            print(target.name, "HP :", str(target.vitality) + "/" + str(target.total_vitality))

            target.check_life()
            # Check if target is dead. If so, mark them as such.
            print()
        else:
            return


class Magician(Caster):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=35, strength=4, agility=8, defense=5,
                         intelligence=8, spirit=8, magic_points=10)


class Bard(Caster):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=40, strength=4, agility=10, defense=7,
                         intelligence=6, spirit=8, magic_points=9)


class Darkmage(Caster):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=30, strength=4, agility=8, defense=5,
                         intelligence=12, spirit=6, magic_points=12)


# TODO Mechanic classes (base)
