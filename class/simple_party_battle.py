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


def battle_menu(player_party, enemy_party):
    for character in player_party:
        character.battle_command_list()
    for enemy in enemy_party:
        enemy.battle_command_list()
