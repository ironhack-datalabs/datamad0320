
import random


# Soldier


class Soldier:
    def __init__ (self,health, strength):
        self.health= health
        self.strength= strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name=name

    def receiveDamage(self, damage):
        Soldier.receiveDamage(self, damage)
        if self.health>0:
            return(f"{self.name} has received {damage} points of damage")
        else:
            return(f"{self.name} has died in act of combat")
            
    def battleCry(self):
        return "Odin Owns You All!"



# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        Soldier.receiveDamage(self, damage)
        if self.health>0:
            return(f"A Saxon has received {damage} points of damage")
        else:
            return(f"A Saxon has died in combat")




# War


class War:
    def __init__ (self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking (self, viking=1):
        self.vikingArmy.append(viking)

    def addSaxon (self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viking= random.choice(self.vikingArmy)

        random_saxon=random.randint(0, len(self.saxonArmy)-1)

        self.saxonArmy[random_saxon].receiveDamage(Viking.strength)
        if self.saxonArmy[random_saxon].health < 1:
            self.saxonArmy.pop(random_saxon)
            return "A Saxon has died"

    def saxonAttack(self):
        Saxon= random.choice(self.saxonArmy)

        random_viking=random.randint(0, len(self.vikingArmy)-1)

        self.vikingArmy[random_viking].receiveDamage(Saxon.strength)
        if self.vikingArmy[random_viking].health < 1:
            self.vikingArmy.pop(random_viking)
            return "A Viking has died"



    def showStatus(self):
        if len(self.saxonArmy)== 0:
            return "Vikings have won the war of the century!"
        if len (self.vikingArmy)== 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) >1 and len(self.vikingArmy)>1 :
            return "Vikings and Saxons are still in the thick of battle."
