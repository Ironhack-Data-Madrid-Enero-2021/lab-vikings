
import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage 


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        if self.vikingArmy and self.saxonArmy:
            vikSold = random.choice(self.vikingArmy)
            saxSold = random.choice(self.saxonArmy)
            vikAttack = vikSold.strength
            battle = saxSold.receiveDamage(vikAttack)
            if saxSold.health <= 0:
                self.saxonArmy.remove(saxSold)
            return battle

    def saxonAttack(self):
        if self.vikingArmy and self.saxonArmy:
            vikSold = random.choice(self.vikingArmy)
            saxSold = random.choice(self.saxonArmy)
            saxAttack = saxSold.strength
            clash = vikSold.receiveDamage(saxAttack)
            if vikSold.health <= 0:
                self.vikingArmy.remove(vikSold)
            return clash
    
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

    pass
