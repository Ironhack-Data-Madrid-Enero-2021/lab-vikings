import random
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health-=damage
            
# Viking

class Viking (Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
    
# War

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        random.shuffle(self.vikingArmy)
        random.shuffle(self.saxonArmy)
        viking_fighter=self.vikingArmy[0]
        saxon_fighter=self.saxonArmy[0]
        attack=viking_fighter.attack()
        if saxon_fighter.health <= attack:
            self.saxonArmy.pop(0)
        return saxon_fighter.receiveDamage(attack)
    def saxonAttack(self):
        random.shuffle(self.vikingArmy)
        random.shuffle(self.saxonArmy)
        viking_fighter=self.vikingArmy[0]
        saxon_fighter=self.saxonArmy[0]
        attack=saxon_fighter.attack()
        if viking_fighter.health <= attack:
            self.vikingArmy.pop(0)
        return viking_fighter.receiveDamage(attack)
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif (len(self.saxonArmy) != 0) and (len(self.vikingArmy) != 0):
            return "Vikings and Saxons are still in the thick of battle."