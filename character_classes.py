from mob_class import *


class Player(Mob):
    """Base human class"""
    def __init__(self, name, vitality, strength, agility, defense):
        super().__init__(name, vitality, strength, agility, defense)


class Hoplite(Player):
    """Base spear-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=50, strength=10, agility=4, defense=0)


class Soldier(Player):
    """Base sword-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=40, strength=9, agility=7, defense=0)


class FistFighter(Player):
    """Base fist-fighting class"""
    def __init__(self, name):
        super().__init__(name, vitality=30, strength=9, agility=9, defense=10)
