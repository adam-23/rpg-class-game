from main_mob_class import *


class Player(Mob):
    """Base human class"""


# Warrior Classes
class Fighter(Player):
    var = None


class Hoplite(Fighter):

    """Base spear-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=55, strength=12, agility=5, defense=8,
                         intelligence=4, spirit=4, magic_points=2)

    def special_command(self, target):
        specialty_name = "[Pierce]"

        orig_strength = self.strength
        target_orig_defense = target.defense

        self.strength *= 1.2
        target.defense = 0.8

        print(specialty_name)
        self.attack(target)

        self.strength = orig_strength
        target.defense = target_orig_defense


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
    var = None


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

    backRow = True


class Rogue(Thief):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=40, strength=9, agility=13, defense=7,
                         intelligence=4, spirit=4, magic_points=2)


# Caster classes (base)
class Caster(Player):
    def reduce_magic_points(self, reduction_number):
        self.magic_points -= reduction_number
        return self.magic_points

    def print_magic_points(self):
        print(self.name, "MP :", str(self.magic_points) + "/" + str(self.total_magic_points))

    def pulse(self, target):
        if target.is_alive and self.is_alive and self.magic_points > 1:
            # Check if target and attacker are both alive, else attack is cancelled.

            self.reduce_magic_points(1)
            # Reduce by 1

            miss = self.check_miss(target)
            if miss:
                return
                # Check if hit or miss

            total_damage_given = 0

            damage_given = (self.intelligence * self.spirit) / ((target.intelligence + target.spirit) / 4)
            damage_given = randomize_damage(damage_given)

            # Check if alive after reduction
            # Print damage
            total_damage_given += damage_given

            print(self.name, "cast Pulse on", target.name + "!")
            self.print_magic_points()
            self.reduce_vitality(target, total_damage_given)

            target.check_life()
            # Check if target is dead. If so, mark them as such.
            print()
        else:
            print("One is dead. Spell cancelled.")
            return

    backRow = True


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
