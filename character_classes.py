from mob_class import *


class Player(Mob):
    """Base human class"""
    def __init__(self, name, vitality, strength, agility, defense):
        super().__init__(name, vitality, strength, agility, defense)


# Warrior Classes
class Hoplite(Player):
    """Base spear-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=55, strength=12, agility=5, defense=8)


class Soldier(Player):
    """Base sword-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=50, strength=12, agility=7, defense=8)


class FistFighter(Player):
    """Base fist-fighting class"""
    def __init__(self, name):
        super().__init__(name, vitality=45, strength=12, agility=11, defense=8)


# Rogue classes (base)
class Scout(Player):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=45, strength=8, agility=15, defense=7)


class Archer(Player):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=35, strength=7, agility=13, defense=7)
        # TODO add row system
        # TODO make Archer unaffected by range in rows


class Rogue(Player):
    """Base fist-fighting class"""

    def __init__(self, name):
        super().__init__(name, vitality=40, strength=9, agility=13, defense=7)

# TODO Caster classes (base)

# TODO Mechanic classes (base)
