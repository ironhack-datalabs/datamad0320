
# Soldier

class Soldier:
    # constructor function with two arguments: "soldier_health" and "soldier_strength"
    # argument "self" by defect
    def __init__(self, soldier_health, soldier_strength):
        self.health=soldier_health       # 1st Soldier property: health
        self.strength=soldier_strength   # 2nd Soldier property: strength

    # Method "attack()" with 0 arguments
    def attack(self):
        return self.strength
    
    # Method "receiveDamage()" with one argument: "damage"
    def receiveDamage(self, damage):
        self.health+= (-damage)




# Viking

#METER SUPER INIT EN LA __INIT__

# class Viking is a subclass of Soldier.
class Viking (Soldier):
    # Construction function with three arguments: name, health, and strength
    def __init__(self, viking_name, viking_health, viking_strength): #Por qué en este orden??
        #super().__init__(self, viking_health, viking_strength)
        self.name=viking_name           # 1st Viking property: name
        self.health=viking_health       # 2nd Viking property: health
        self.strength=viking_strength   # 3rd Viking property: strength
        
    # Method "attack()" inherit from Soldier

    # Method "receiveDamage()" is different from the one inherit from Soldier
    def receiveDamage(self, damage):
        self.health += (-damage)

        if self.health >0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    # Method "battleCry()"
    def battleCry(self):
        return f"Odin Owns You All!"




# Saxon

# class Saxon is a subclass of Soldier.
class Saxon (Soldier):
    def __init__(self, saxon_health, saxon_strength):
        self.health=saxon_health       # 1st Saxon property: health
        self.strength=saxon_strength   # 2nd Saxon property: strength

    # Method "attack()" inherit from Soldier

    # Method "receiveDamage()" is different from the one inherit from Soldier
    def receiveDamage(self, damage):
        self.health += (-damage)

        if self.health >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"



# War


class War:
    pass
