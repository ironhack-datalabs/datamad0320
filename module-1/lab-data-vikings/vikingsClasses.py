
import random 

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health-=damage

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name  
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

class Saxon(Soldier):
    def __init__(self, health, strength): #Parámetros que le voy a dar la soldier + nuevos parámetros 
        super().__init__(health, strength) #Parámetros que recibe la función Soldier
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        i_v=random.choice(range(len(self.vikingArmy)))
        i_sx=random.choice(range(len(self.saxonArmy)))
        viking=self.vikingArmy[i_v]
        saxon=self.saxonArmy[i_sx]
        health_mod=saxon.health-viking.strength
        if health_mod<=0:
            self.saxonArmy.pop(i_v)
        else:
            pass
        return saxon.receiveDamage(viking.strength)
        
    def saxonAttack(self):
        i_v=random.choice(range(len(self.vikingArmy)))
        i_sx=random.choice(range(len(self.saxonArmy)))
        viking=self.vikingArmy[i_v]
        saxon=self.saxonArmy[i_sx]
        health_mod=viking.health-saxon.strength
        if health_mod<=0:
            self.vikingArmy.pop(i_sx)
        else:
            pass
        return viking.receiveDamage(saxon.strength)
       
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."