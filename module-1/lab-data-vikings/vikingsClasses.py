
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
    def __init__(self, name, health, strength):
        Soldier.__init__(self,health, strength)
        self.name = name
  
    def receiveDamage(self,damage):
        self.health = self.health - damage
        result = ""
        if self.health > 0:
            result += f"{self.name} has received {damage} points of damage"
        else: 
            result += f"{self.name} has died in act of combat"
        
        return result

    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

        
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health = self.health - damage
        result = ""
        if self.health > 0:
            result = f"A Saxon has received {damage} points of damage"
        else: 
            result = "A Saxon has died in combat"
        return result

# War

class War:
    def __init__(self):
        pass
    def addViking():
     pass
    def addSaxon():
        pass
    def vikingAttack():
        pass
    def saxonAttack():
        pass
    def showStatus():
        pass