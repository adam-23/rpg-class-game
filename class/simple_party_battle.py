from character_classes import *

from monster_classes import *

rat1 = Rat()
darkmage1 = Darkmage("Darkmage")
Soldier1 = Soldier("Soldier")

combatants = []
for combatant in combatants:
    if combatant.backRow:
        combatant.is_melee_target = False

    # TODO input for different commands:
    # TODO Attack
    # TODO Item
    # TODO Defend
    # TODO Run Away
    # TODO Magic
    # TODO Class-specific commands
# TODO If combatant is in the back row and they have melee front units, combatant is not a melee target.


current_player_party = []
current_enemy_party = []

'''
Pseudocode for the random encounter battle script:
    1. you have heros
       you have enemies
    2. every hero gets their menu pick for the command
       every enemy randomly picks one of their actions
    3. order every mob based on current speed
    4. carry out every turn in order
    5. Test for github bc I can't make it all work

'''


def battle_menu(player_party, enemy_party):
    for character in player_party:
        character.battle_command_list()
    for enemy in enemy_party:
        enemy.battle_command_list()
