
import random
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health = self.health - damage
        return None     

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength) 
        self.name = name

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        

    def  battleCry(self): 
        return f"Odin Owns You All!"


# Saxon


class Saxon (Soldier):
    def __init__(self,health,strength):
        super().__init__(health, strength)

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"    


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        self.viking_attacker = random.choice(self.vikingArmy)
        self.saxon_reciever = random.choice(self.saxonArmy)
        self.battle = self.saxon_reciever.receiveDamage(self.viking_attacker.strength)
        if self.saxon_reciever.health <= 0:
            self.saxonArmy.remove(self.saxon_reciever)
        return self.battle

    def saxonAttack(self):
        self.saxon_attacker = random.choice(self.saxonArmy)
        self.viking_reciever = random.choice(self.vikingArmy)
        self.battle2 = self.viking_reciever.receiveDamage(self.saxon_attacker.strength)
        if self.viking_reciever.health <= 0:
            self.vikingArmy.remove(self.viking_reciever)
        return self.battle2

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."




    
