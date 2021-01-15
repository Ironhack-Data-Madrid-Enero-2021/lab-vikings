
# Soldier

class Soldier:
    def _init_(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
