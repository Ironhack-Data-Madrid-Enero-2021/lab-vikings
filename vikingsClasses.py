
"""if isinstance() returns:
- True if the object is an instance or subclass of a class or any element of the tuple
- False otherwise
- If classinfo is not a type or tuple of types, a TypeError exception is raised."""

import random
"""nota uso: random.choice(myList) = elemento aleatorio de una lista"""

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
        if self.health >= 0:
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
        if self.health >= 0:
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
        v1 = random.choice(self.vikingArmy)
        s1 = random.choice(self.saxonArmy)

        damage_saxon = s1.receiveDamage(v1.attack())

        if s1.health > 0:
            self.saxonArmy.remove(s1)
            return "result of calling " + str(s1.receiveDamage) + " of a Saxon with the strength of a Viking"
      

    def saxonAttack(self):
        v2 = random.choice(self.vikingArmy)
        s2 = random.choice(self.saxonArmy)

        damame_viking = v2.receiveDamage(s2.attack()) 

    
        if v2.health > 0:
            self.vikingArmy.remove(v2)
            return "result of calling " + str(v2.receiveDamage) + " of a Viking with the strength of a Saxon"
        

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

