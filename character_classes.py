from mob_class import *


class Player(Mob):
    """Base human class"""
    def __init__(self, name, vitality, strength, agility, defense):
        super().__init__(name, vitality, strength, agility, defense)


# Warrior Classes

class Hoplite(Player):
    """Base spear-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=50, strength=10, agility=5, defense=8)


class Soldier(Player):
    """Base sword-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=40, strength=10, agility=7, defense=8)


class FistFighter(Player):
    """Base fist-fighting class"""
    def __init__(self, name):
        super().__init__(name, vitality=35, strength=11, agility=11, defense=8)


#TODO Rogue classes (base)

#TODO Caster classes (base)

#TODO Mechanic classes (base)
