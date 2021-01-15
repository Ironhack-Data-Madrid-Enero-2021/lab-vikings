
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


class Saxon:
    pass

# War


class War:
    pass
