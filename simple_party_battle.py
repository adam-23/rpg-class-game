from character_classes import *

darkmage1 = Darkmage("Darkmage")
Soldier1 = Soldier("Soldier")

combatants = []
for combatant in combatants:
    if combatant.backRow:
        combatant.is_melee_target = False

# TODO If combatant is in the back row and they have melee front units, combatant is not a melee target.
