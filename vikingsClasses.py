
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
    pass
