from mob_class import *


class Monster(Mob):
    """Base monster class"""
    def __init__(self, name, vitality, strength, agility):
        super().__init__(name, vitality, strength, agility)


class Rat(Monster):
    """Shitty little rats."""
    def __init__(self):
        super().__init__(name="Rat", vitality=8, strength=4, agility=2)
