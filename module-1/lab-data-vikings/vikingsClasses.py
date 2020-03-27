
# Soldier


class Soldier:
    # constructor function with two arguments: "soldier_health" and "soldier_strength"
    # argument "self" by defect
    def __init__(self, soldier_health, soldier_strength):
        self.health=soldier_health       # 1st Soldier property: health
        self.strength=soldier_strength   # 2nd Soldier property: strength

    # Method 1 with 0 arguments
    def attack(self):
        return self.strength
    
    # Method 2 with one argument: "damage"
    def receiveDamage(self, damage):
        self.health+= (-damage)

# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
