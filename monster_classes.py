from mob_class import *


class Monster(Mob):
    """Base monster class"""

    def __init__(self, name, vitality, strength, agility, defense, intelligence, spirit, magic_points):
        super().__init__(name, vitality, strength, agility, defense, intelligence, spirit, magic_points)


class Rat(Monster):
    """Annoying little rats."""
    def __init__(self):
        super().__init__(name="Rat", vitality=8, strength=4, agility=2, defense=0,
                         intelligence=0, spirit=0, magic_points=0)
