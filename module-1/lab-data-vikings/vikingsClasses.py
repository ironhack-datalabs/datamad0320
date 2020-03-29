
import random
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

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.Viking = Viking
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.Saxon = Saxon
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        randomViking = random.choice(self.vikingArmy)
        randomSaxon = random.choice(self.saxonArmy)
        receivedDamage = randomSaxon.receiveDamage(randomViking.strength)
        if randomSaxon.health <= 0:
            self.saxonArmy.remove(randomSaxon)
            
        return receivedDamage
        
    def saxonAttack(self):
        randomViking = random.choice(self.vikingArmy)
        randomSaxon = random.choice(self.saxonArmy)
        receivedDamage = randomViking.receiveDamage(randomSaxon.strength)
        if randomViking.health <= 0:
            self.vikingArmy.remove(randomViking)

        return receivedDamage
    
    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
            return"Vikings have won the war of the century!"
             
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
            
        