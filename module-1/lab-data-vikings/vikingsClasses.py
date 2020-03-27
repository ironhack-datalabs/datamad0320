
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

# class Viking is a subclass of Soldier.
class Viking (Soldier):
    # Construction function with three arguments: name, health, and strength
    def __init__(self, viking_name):
        # 1st Viking property: health (inherit from Soldier)
        # 2nd Viking property: strength (inherit from Soldier)
        self.name=viking_name   #3rd Viking property: name

    # Method "attack" inherit from Soldier

    # Method "receiveDamage" is different from the one inherit from Soldier
    def receiveDamage(self, damage):
        self.health+= (-damage)
        if self.health>0:
            return (f"{self.name} has received {damage} points of damage")





# Saxon


class Saxon:
    pass

# War


class War:
    pass
