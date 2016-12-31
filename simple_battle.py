from character_classes import *
from monster_classes import *

fist1 = FistFighter("Fistfighter")
spear1 = Hoplite("Hoplite")
rat1 = Rat()


spear1.attack(fist1)
fist1.attack(spear1)