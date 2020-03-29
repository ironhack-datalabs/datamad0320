
# Soldier
import random

class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # add code here
    
    
    def attack(self):
        return self.strength 
    
    
    def receiveDamage(self,damage):
        self.health -= damage

        
    
    
    
# Viking  1


class Viking(Soldier):
    
    
    def __init__(self, name, health, strength):
        
        self.name=name
        super().__init__(health,strength)
        
        
    def attack(self):
        return super().attack()
    
    
    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        print(self.health)
        
        if self.health >0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
        
        
    def battleCry(self):
        return "Odin Owns You All!"
    
    
    
    
    
    
    
    # Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        
        super().__init__(health,strength)
        
    
    
    def attack(self):
        return super().attack()
    
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


    
# War


class War:
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        
    def addViking(self, Viking):
        
        self.vikingArmy.append(Viking)
        
        
        
    def addSaxon(self,Saxon):
        
        self.saxonArmy.append(Saxon)
        
        
    def vikingAttack(self):
        saxon_soldier = random.choice(self.saxonArmy)
        
        viking_soldier = random.choice(self.vikingArmy)
        
        saxon_soldier.receiveDamage(viking_soldier.attack())
        
        if saxon_soldier.health <= 0:
            
            self.saxonArmy.remove(saxon_soldier)
            return "A Saxon has died in combat"
        
        
        
    def saxonAttack(self):
        
        saxon_soldier = random.choice(self.saxonArmy)
        
        viking_soldier = random.choice(self.vikingArmy)
        
        viking_soldier.receiveDamage(saxon_soldier.attack())
        
        if viking_soldier.health <= 0:
            self.vikingArmy.remove(viking_soldier)
            
        return f"{viking_soldier.name} has received {saxon_soldier.strength} points of damage"

        
        
    def showStatus(self):
        
        if (len(self.vikingArmy) > 0 and len(self.saxonArmy) == 0):
            return "Vikings have won the war of the century!"
        
        elif (len(self.vikingArmy) == 0 and len(self.saxonArmy) >0):
            return "Saxons have fought for their lives and survive another day..."     
        elif (len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0):
            return "Vikings and Saxons are still in the thick of battle."
    
    

