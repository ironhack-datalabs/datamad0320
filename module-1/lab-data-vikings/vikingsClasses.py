
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
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        return Saxon.receiveDamage(Viking.streng)
        
    def saxonAttack(self):
        return Viking.receiveDamage(Saxon.streng)
    
    def showStatus(self):
        result = ""
        if len(self.vikingArmy) == 0:
            result += "Vikings have won the war of the century!"
        else:
            result += "Vikings and Saxons are still in the thick of battle."
        if len(self.saxonArmy) == 0:
            result += "Saxons have fought for their lives and survive another day..."
        else:
            result += "Vikings and Saxons are still in the thick of battle."
        return result