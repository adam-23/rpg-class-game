from mob_class import *


class Monster(Mob):
    """Base monster class"""
    def __init__(self, name, vitality, strength, agility, defense):
        super().__init__(name, vitality, strength, agility, defense)


class Rat(Monster):
    """Annoying little rats."""
    def __init__(self):
        super().__init__(name="Rat", vitality=8, strength=4, agility=2, defense=0)
