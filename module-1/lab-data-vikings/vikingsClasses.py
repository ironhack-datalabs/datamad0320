
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name):
        self.name = name
        super().__init__(health, strength)

# Saxon


class Saxon:
    pass

# War


class War:
    pass
