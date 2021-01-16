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
    
    VikingArmy = []
    SaxonArmy = []


    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.SaxonArmy.append(saxon)

    def vikingAttack(self):
        V = random.choice(self.viking_army)
        S = random.choice(self.saxonArmy)



        if saxon.health <= 0:
            self.saxon.remove(s)
    
    def saxonAttack(self):
        V = random.choice(self.viking_army)
        S = random.choice(self.saxonArmy)

        if viking.health <= 0:
            self.viking.remove(v)

    def showStatus(self):
        if len(self.SaxonArmy) == 0:
            return f"Vikings have won the war of the century!"

        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        
        else:
            return f"Vikings and Saxons are still in the thick of battle."


    
