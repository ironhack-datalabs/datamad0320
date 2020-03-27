#
# Soldier

    
class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength = strength
    def Atack(self):
        return self.strength
    def ReceiveDamage(self,damage):
         
        self.damage = damage
        newhealth = health - damage
        pass
soldier = Soldier(30,50)
print(soldier)
# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
