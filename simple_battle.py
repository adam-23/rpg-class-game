from character_classes import *
from monster_classes import *

npc = FistFighter("NPC Bob")
adam = Hoplite("Adam")
rat1 = Rat()

rat1.attack(adam)
adam.attack(rat1)
adam.attack(npc)

rat1.attack(adam)
adam.attack(rat1)
adam.attack(npc)

rat1.attack(adam)
adam.attack(rat1)
adam.attack(npc)
