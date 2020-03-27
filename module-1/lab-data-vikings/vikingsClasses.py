
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
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        super().attack()

    def receiveDamage(self, damage):
        super().receiveDamage()
        if self.health > 0:
            return f"{name} has received {damage} points of damage"
        else:
            return f"{name} has died in act of combat"


    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon:
    pass



# War
class War:
    pass
