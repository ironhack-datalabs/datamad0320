#
# Soldier
import random
    
class Soldier:
        
    def __init__(self, health, strength):
        self.health= health
        self.strength = strength
            
    def attack(self):   
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        if self.health >= self.damage:
            self.health -= damage
            
       
         
                                           
          
 
        

# Viking

class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__( health, strength)
        self.name = name
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        if self.health > self.damage:
            self.health -= self.damage
            
            return f"{self.name} has received {damage} points of damage"
        else :
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self,health, strength):
        self.health= health
        self.strength = strength  
        
   
    def attack(self):
        return self.strength 
         
    
    def receiveDamage(self,damageSaxo):
        self.damageSaxo = damageSaxo
        if self.health > self.damageSaxo:
            self.health -= self.damageSaxo
            
            return f"A Saxon has received {damageSaxo} points of damage"
        else :
            return f"A Saxon has died in combat"   





# War


class War:
    def __init__(self):
      self.vikingArmy = []
      self.saxonArmy = []
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        self.saxon = random.choice(self.saxonArmy)
        self.viking = random.choice(self.vikingArmy)
        self.saxon.receiveDamage(self.viking.attack)
        if self.saxon["health"] <= 0:
            self.saxonArmy.remove(self.saxon)
        return f"Saxon {recibedamage.viking.attack()}"

    def saxonAttack(self):
        self.saxon = random.choice(self.saxonArmy)
        self.viking = random.choice(self.vikingArmy)
        self.viking.receiveDamage(self.saxon.attack)
        if self.viking['health'] <= 0:
            self.vikingArmy.remove(self.viking)
        return f"{viking['name']} {recibedamage.saxon.attack()}"

    def showStatus(self):
        if self.saxonArmy() ==  0:
            return f"Vikings have won the war of the century!"
        
        elif self.vikingArmy() == 0 :
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."
##Prueba que no sube al repositorio