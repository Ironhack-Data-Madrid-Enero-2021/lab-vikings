import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health = self.health - damage
    
# Viking
class Viking:
    def __init__ (self, name, health, strength):
        Soldier. __init__(self, health, strength)
        self.name = name
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return str(self.name) + " has received " + str(damage) + " points of damage"
        else:
            return str(self.name) + " has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon:
    def __init__ (self, health, strength):
        Soldier. __init__(self, health, strength)

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
# War
class War:
    def __init__ (self): 
        self.vikingArmy = []
        self.saxonArmy= []

    def addViking(self,viki):
        if isinstance(viki,Viking):
            self.vikingArmy.append(viki)

    def addSaxon(self,saxo):
        if isinstance(saxo,Saxon):
            self.saxonArmy.append(saxo)
   
    def vikingAttack(self):
        v = random(self.vikingArmy)
        s = random(self.saxonArmy)

        v.receiveDamage = s.strength

        if s.health <= 0:
            self.saxonArmy.remove(s)
        
        return "result of calling " + str(receiveDamage) + "of a Saxon with the strength of a Viking"

    def saxonAttack(self):
        v = random(self.vikingArmy)
        s = random(self.saxonArmy)

        v.receiveDamage = s.strength

        if v.health <= 0:
            self.vikingArmy.remove(v)
        
        return "result of calling " + str(receiveDamage) + "of a Viking with the strength of a Saxon"

    def showStatus(self):
        if self.saxonArmy == 0:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

