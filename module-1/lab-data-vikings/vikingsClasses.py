# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    # Aquí van los métodos
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
       
    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)

        # Aquí van los métodos


        
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
