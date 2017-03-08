while len(enemies) > 0:
    if len(heros) == 0:
        print("You died. Returning to game menu....")

    for hero in heros:
        hero.battle_command_list(enemies)
        if __name__ == '__main__':
            enemy_check # function that checks if enemies are alive or not, and remove them if not




"""
World map program
    walk -> battle program
    menu program
        save current party variables (export all party variables as CSV/json)
        change equipment -> change party equipment variables
        change row variables
        view magic, use spells
        view items, use items
        combine items
        view map, current location

"""

"""
Battle program
    loads terrain
    loads enemies based on terrain
    loads heros from status sheet
        enemies and heros fight
        if enemy dies, it gets removed from the field
        if hero dies, they get put into the revive zone
            if all heros die, game over
            if all enemeies die, rewards are distributed and the battle program ends
"""