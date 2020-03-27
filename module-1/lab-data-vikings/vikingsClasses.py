
import random
# Soldier


class Soldier:

    def __init__(self, health, strength):      
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength


    def receiveDamage(self,damage):
        self.health=self.health-damage
        
  

# Viking


class Viking(Soldier):
    
    def __init__(self,name, health, strength):
        super().__init__(health,strength)
        self.name=name

    def receiveDamage(self,damage):
        
        self.health=self.health-damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health,strength)
        

    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
class War():
    def __init__(self):    
        self.vikingArmy=[]
        self.saxonArmy =[]
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        damage=random.choice(self.vikingArmy).attack()
        saxon=random.choice(self.saxonArmy)
        answer=saxon.receiveDamage(damage)

        if saxon.health<=0:
            self.saxonArmy.remove(saxon)
        return answer


    def saxonAttack(self):
        damage=random.choice(self.saxonArmy).attack()
        viking=random.choice(self.vikingArmy)
        answer=viking.receiveDamage(damage)

        if viking.health<=0:
            self.vikingArmy.remove(viking)
        return answer
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



