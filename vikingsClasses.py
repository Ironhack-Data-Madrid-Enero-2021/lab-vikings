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
    
    pass

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name    
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
    



# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength) 

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"     
    
 
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        if self.vikingArmy and self.saxonArmy:
            escoge_v = random.choice(self.vikingArmy)
            escoge_s = random.choice(self.saxonArmy)
            
            ataque_v = escoge_v.strength
            lucha = escoge_s.receiveDamage(ataque_v)
            if escoge_s.health <= 0:
                self.saxonArmy.remove(escoge_s)
            return lucha
 
    def saxonAttack(self):
        if self.vikingArmy and self.saxonArmy:
            escoge_s = random.choice(self.saxonArmy)
            escoge_v = random.choice(self.vikingArmy)

            ataque_s = escoge_s.strength
            batalla = escoge_v.receiveDamage(ataque_s)
            if escoge_v.health <= 0:
                self.vikingArmy.remove(escoge_v)
            return batalla
   
   
    def showStatus(self):
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

