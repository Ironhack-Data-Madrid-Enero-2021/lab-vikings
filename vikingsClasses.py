
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        return
        
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        self.strength
        return self.strength

    def receiveDamage(self, damage): # estos métodos tienen que ser reimplentados ==> esto, si no he entenido mal se hace sobreeribiendo la variable como se hace a continuación
        #Basicamente, estoy llamando a la clase constructora para definir todos los valores, pero luego anulo el valor (health y damage) de esta clase
        self.damage = damage
        self.health = self.health - damage


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

    def attack(self):
        self.strength
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"

        else:
            return f"A Saxon has died in combat"
    
# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

        #aqui creo que deberia ir algo
    
    def addViking(self, Viking):

        self.vikingArmy.append(Viking)

    
    def addSaxon(self, Saxon):
        
        self.vikingArmy.append(Viking)

        pass
