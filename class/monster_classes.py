from main_mob_class import *


class Monster(Mob):
    """Base monster class"""

    def __init__(self, name, vitality, strength, agility, defense, intelligence, spirit, magic_points):
        super().__init__(name, vitality, strength, agility, defense, intelligence, spirit, magic_points)


class Rat(Monster):
    """Annoying little rats."""
    def __init__(self):
        super().__init__(name="Rat", vitality=8, strength=4, agility=2, defense=0,
                         intelligence=0, spirit=0, magic_points=0)


class Impus(Monster):
    """Hostile fey. Some people view them as cute."""

class Imp(Impus):
    """Basic imp archetype. Annoying but not threatening."""

    def __init__(self):
        super().__init__(name="Imp", vitality=20, strength=6, agility=5, defense=2,
                         intelligence=3, spirit=3, magic_points=2)


# fuckingtestforgithub
class Pugilimp(Impus):
    """Imp with a massive fist. Powerful and agressive, but fragile."""

    def __init__(self):
        super().__init__(name="Pugilimp", vitality=42, strength=9, agility=4, defense=3,
                         intelligence=1, spirit=1, magic_points=1)


class Geismite(Monster):
    """Surreal ghost-like creatures that attack humans on sight."""

    def __init__(self):
        super().__init__(name="Geismite", vitality=25, strength=8, agility=8, defense=3,
                         intelligence=6, spirit=6, magic_points=12)


class Urkrab(Monster):
    """Bear Crabs. Powerful with strong shells, but make tasty stews."""

    def __init__(self):
        super().__init__(name="Urkrab", vitality=50, strength=15, agility=2, defense=8,
                         intelligence=0, spirit=0, magic_points=0)


class Plamud(Monster):
    """Flatmouth. A flat hunk of amorphous digestive tissue with a well-developed jaw."""

    def __init__(self):
        super().__init__(name="Plamud", vitality=20, strength=5, agility=1, defense=0,
                         intelligence=0, spirit=0, magic_points=0)


class Okralor(Monster):
    """Literally an Eye-Crawler. Well developed eyes and brain inside a chitin exoskeleton."""

    def __init__(self):
        super().__init__(name="Okralor", vitality=24, strength=6, agility=8, defense=3,
                         intelligence=0, spirit=0, magic_points=0)
