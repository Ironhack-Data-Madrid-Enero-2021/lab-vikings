import random


# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength


    def attack(self):
        return self.strength

    def receiveDamage(self,thedamage):
        self.health = self.health - thedamage

    



# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength


    def receiveDamage(self, thedamagev):
        self.health = self.health - thedamagev
        if self.health > 0:
            return f"{self.name} has received {thedamagev} points of damage"
        else:
            return f"{self.name} has died in act of combat"


    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, thedamages):
        self.health = self.health - thedamages
        if self.health > 0:
            return f"A Saxon has received {thedamages} points of damage"
        else:
            return "A Saxon has died in combat"



    
# War


class War:
    
    def __init__(self):
        self.vikingArmy  = []
        self.saxonArmy = []


    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    

    def vikingAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)


        result_sax = sax.receiveDamage(vik.strength)

        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        
        return result_sax



    def saxonAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)


        result_vik = vik.receiveDamage(sax.strength)

        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        
        return result_vik

        

    def showStatus(self):
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        
        else: 
            return "Saxons have fought for their lives and survive another day..."
        
        


