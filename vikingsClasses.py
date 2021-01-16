import random
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage



# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health  -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return f"Odin Owns You All!"

        
# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health  -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"



    

# War


class War:
    
    vikingArmy = []
    saxonArmy = []


    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        Vik = random.choice(self.vikingArmy)
        Sax = random.choice(self.saxonArmy)
        
        theWar = Sax.receiveDamage(Vik.strength)

        if Sax.health <= 0:
            self.saxonArmy.remove(Sax)
        else:
            return theWar
    
    def saxonAttack(self):
        Vik = random.choice(self.vikingArmy)
        Sax = random.choice(self.saxonArmy)

        thewar2 = Vik.receiveDamage(Sax.strength)
        
        if Vik.health <= 0:
            self.vikingArmy.remove(Vik)
        else:
            return thewar2

    def showStatus(self):
        if not self.saxonArmy:
            return f"Vikings have won the war of the century!"

        if not self.vikingsArmy:
            return f"Saxons have fought for their lives and survive another day..."
        
        else:
            return f"Vikings and Saxons are still in the thick of battle."


    
