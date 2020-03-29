
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
    
    def addViking (self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon (self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        random_viking = self.vikingArmy[random.randint(0, len(self.vikingArmy) - 1)]  # Viking + index
        random_saxon = self.saxonArmy[random.randint(0, len(self.saxonArmy) - 1)]  # saxon + index

        viking_attack = random_viking.attack()  # viking attack
        saxon_damage = random_saxon.receiveDamage(viking_attack)  # viking attack=saxon damage

        if random_saxon.health < 1:
            self.saxonArmy.remove(random_saxon)
            return "A Saxon has died in combat"
        
        return saxon_damage


    def saxonAttack(self):
        random_viking = self.vikingArmy[random.randint(0, len(self.vikingArmy) - 1)]  # Viking + index
        random_saxon = self.saxonArmy[random.randint(0, len(self.saxonArmy) - 1)]  # saxon + index

        saxon_attack = random_saxon.attack()  # saxon attack
        viking_damage = random_viking.receiveDamage(saxon_attack)  # viking attack=saxon damage

        if random_viking.health < 1:
            self.vikingArmy.remove(random_viking)
            return "A Viking has died"
            
        return viking_damage

    def showStatus(self):
        if len(self.saxonArmy)== 0:
            return "Vikings have won the war of the century!"
        if len (self.vikingArmy)== 0:
            return "Saxons have fought for their lives and survive another day..."
        if (len(self.saxonArmy) >0) and (len(self.vikingArmy)>0) :
            return "Vikings and Saxons are still in the thick of battle."
