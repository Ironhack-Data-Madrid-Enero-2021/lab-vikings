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
        self.name = name
        self.health = health
        self.strength = strength

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
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

    

# War


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)#Añado un vikingo

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)#Añado un sajon

    def vikingAttack(self):
        saxon_random = random.choice(self.saxonArmy)#Llamo a un sajon aleatorio
        viking_random= random.choice(self.vikingArmy)#Llamo a un vikingo aleatorio
        
        #Creo una variable que almacena el daño que hace un vikingo
        viking_attack = saxon_random.receiveDamage(viking_random.attack())
        if saxon_random.health <= 0:
            self.saxonArmy.remove(saxon_random)#Si el sajon no tiene vida se elimina

        return viking_attack

    def saxonAttack(self):
        saxon_random = random.choice(self.saxonArmy)
        viking_random = random.choice(self.vikingArmy)

        saxon_attack = viking_random.receiveDamage(saxon_random.attack())

        if viking_random.health <= 0:
            self.vikingArmy.remove(viking_random)

        return saxon_attack

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"

        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."

        if len(self.vikingArmy) and len(self.saxonArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."







    

