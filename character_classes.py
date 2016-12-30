from mob_class import *


class Player(Mob):
    """Base human class"""
    def __init__(self, name, vitality, strength, agility):
        super().__init__(name, vitality, strength, agility)


class Hoplite(Player):
    """Base spear-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=50, strength=10, agility=4)


class Soldier(Player):
    """Base sword-wielding class"""
    def __init__(self, name):
        super().__init__(name, vitality=40, strength=9, agility=7)


class FistFighter(Player):
    """Base fist-fighting class"""
    def __init__(self, name):
        super().__init__(name, vitality=30, strength=9, agility=9)
