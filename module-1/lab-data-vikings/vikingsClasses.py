
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

class Viking:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if health == 0:
            return (f"{name} has died in act of combat")
        else:
            return (f"{name} has received {damage} points of damage")
    
    def battleCry():
        return f"Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        super().attack(self)

    def receiveDamage(self, damage):
        self.health -= damage
        if health == 0:
            return (f"A Saxon has died in act of combat")
        else:
            return (f"A Saxon has received {damage} points of damage")


# War


class War:
    pass
