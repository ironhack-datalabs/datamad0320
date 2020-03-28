
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return "Odin Owns You All!"
        
            
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

        

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy =[]
    
    def addViking(self):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        saxonsoldier = random.choice(Sanxon.receiveDamage)
        vikingsoldier = random.choice(Viking.self.strength)
        if saxonsoldier == vikingsoldier:
            self.saxonArmy.pop()
        return 
    
    def saxonAttack(self):
        saxonsoldier1 = random.choice(Sanxon.self.strength)
        vikingsoldier2 = random.choice(Viking.receiveDamage)
        if saxonsoldier1 == vikingsoldier2:
            self.vikingArmy.pop()
        return 
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)  == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.vikingArmy) >=1 and len(self.saxonArmy) >=1:
            return "Vikings and Saxons are still in the thick of battle."
