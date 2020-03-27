
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack():
        return self.strength
    
    def receiveDamage(slef, damage):
        self.health = health - damage


# Viking


class Viking:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack():
        return self.strength
    
    def receiveDamage(slef, damage):
        self.health = health - damage
        if health <= 0:
            return ("NAME has received DAMAGE points of damage")


# Saxon


class Saxon:
    pass

# War


class War:
    pass
