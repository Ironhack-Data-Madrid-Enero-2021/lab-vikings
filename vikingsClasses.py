
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


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(self, health, strength)
    
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
