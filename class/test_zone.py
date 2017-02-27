def turn_choice():
    print("A = Attack")
    print("S = Spell")
    print("D = Defend")
    print("F = Flee")
    print()
    move_input = input("move: ").lower()
    print(move_input)
    if move_input == "a":
        print("ATTACK")


turn_choice()
