from character_classes import *

from monster_classes import *

fist1 = FistFighter("Fistfighter")
soldier1 = Soldier("Soldier")
spear1 = Hoplite("Hoplite")
arch1 = Archer("Archer")
rogue1 = Rogue("Rogue")
scout1 = Scout("Scout")
scout2 = Scout("Scout")
scout3 = Scout("Scout")
mage1 = Magician("Magician")
bard1 = Bard("Bard")
darkmage1 = Darkmage("Darkmage")
rat1 = Rat()

"""
spear1.attack(fist1)
fist1.attack(spear1)

soldier1.attack(arch1)
arch1.attack(soldier1)

"""

rogue1.attack(scout1)
scout1.attack(rogue1)

darkmage1.pulse(soldier1)
soldier1.attack(darkmage1)

spear1.special_command(scout3)
spear1.attack(scout2)

# bard1.pulse(scout1)
# mage1.pulse(scout2)
# darkmage1.pulse(scout3)
