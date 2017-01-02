from character_classes import *
from monster_classes import *

fist1 = FistFighter("Fistfighter")
soldier1 = Soldier("Soldier")
spear1 = Hoplite("Hoplite")
arch1 = Archer("Archer")
rogue1 = Rogue("Rogue")
scout1 = Scout("Scout")
rat1 = Rat()


spear1.attack(fist1)
fist1.attack(spear1)

soldier1.attack(arch1)
arch1.attack(soldier1)

rogue1.attack(scout1)
scout1.attack(rogue1)
