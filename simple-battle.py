class Fighter:
    """Base class"""
    def __init__(self, name, vitality, strength, agility):
        self.name = name
        # Name
        self.vitality = vitality
        # Hit points
        self.strength = strength
        # Physical damage
        # TODO add flat physical reduction for beating armored opponents
        # TODO it'll give a difference between strength and dexterity characters
        self.agility = agility
        # Speed
        # TODO add evasiveness for dex characters
        
    is_alive = True
    # Determines if they can act or be acted on
    
    def check_life(self):
        # Check if alive
        
        if self.vitality <= 0:
            print(self.name + " is dead.")
            self.is_alive = False
            # If below, they die.
        
        """elif self.vitality > 0:
            print(self.name + " lives.")
            # If health is above zero, they live"""

    def attack(self, target):
        # Calculate damage given, reduce target vit, check if alive. 
        
        if target.is_alive and self.is_alive:
            # Check if target and attacker are both alive, else attack is cancelled.
            print(self.name, "attacked", target.name + "!")
            damage_given = self.strength * 2
            print(self.name, "dealt " + str(damage_given), "damage!")
            # Calculate damage dealt
        
            print(target.name, "vit", str(target.vitality), "-> ", end='')
            target.vitality -= damage_given
            # Reduce target vitality
            
            if target.vitality >= 0:
                print(str(target.vitality))
            # Print vitality
            else:
                print("0")
                # If vitality is below 0, print 0
        
            target.check_life()
            print()
            # Check if alive after reduction 
        
            return target.vitality
            # Return variables
        
        else:
            return


class Player(Fighter):
    """Base human class"""
    def __init__(self, name):
        super().__init__(name, vitality=64, strength=10, agility=8)
        
# TODO playerclass derivatives HERE


class Monster(Fighter):
    """Base monster class"""
    def __init__(self, name, vitality, strength, agility):
        super().__init__(name, vitality, strength, agility)


class Rat(Monster):
    """Shitty little rats."""
    def __init__(self):
        super().__init__(name="Rat", vitality=8, strength=4, agility=2)

npc = Player("NPC Bob")
adam = Player("Adam")
rat1 = Rat()


rat1.attack(adam)
adam.attack(rat1)

adam.attack(npc)
adam.attack(npc)
adam.attack(npc)
adam.attack(npc)
rat1.attack(npc)
