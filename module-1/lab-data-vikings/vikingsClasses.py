import random



# Soldier

class Soldier:
    # constructor function with two arguments: "soldier_health" and "soldier_strength"
    # argument "self" by defect
    def __init__(self, soldier_health, soldier_strength):
        self.health=soldier_health       # 1st Soldier property: health
        self.strength=soldier_strength   # 2nd Soldier property: strength

    # Method "attack()" with 0 arguments
    def attack(self):
        return self.strength
    
    # Method "receiveDamage()" with one argument: "damage"
    def receiveDamage(self, damage):
        self.health += (-damage)




# Viking

# METER SUPER INIT EN LA __INIT__

# class Viking is a subclass of Soldier.
class Viking (Soldier):
    # Construction function with three arguments: name, health, and strength
    def __init__(self, viking_name, viking_health, viking_strength):
        self.name=viking_name           # 1st Viking property: name
        super().__init__(viking_health, viking_strength)
        #self.health=viking_health       # 2nd Viking property: health
        #self.strength=viking_strength   # 3rd Viking property: strength

    # Method "attack()" inherit from Soldier

    # Method "receiveDamage()" is different from the one inherit from Soldier
    def receiveDamage(self, damage):
        self.health += (-damage)

        if self.health >0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    # Method "battleCry()"
    def battleCry(self):
        return "Odin Owns You All!"




# Saxon

# class Saxon is a subclass of Soldier.
class Saxon (Soldier):
    def __init__(self, saxon_health, saxon_strength):
        super().__init__(saxon_health, saxon_strength)
        #self.health=saxon_health       # 1st Saxon property: health
        #self.strength=saxon_strength   # 2nd Saxon property: strength

    # Method "attack()" inherit from Soldier

    # Method "receiveDamage()" is different from the one inherit from Soldier
    def receiveDamage(self, damage):
        self.health += (-damage)

        if self.health >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"




# War

class War:

    def __init__(self):
        self.vikingArmy = []   # property
        self.saxonArmy = []    # property

    def addViking(self, viking):
        self.vikingArmy += [viking]
        
    def addSaxon(self, saxon):
        self.saxonArmy += [saxon]

    def vikingAttack(self):
        
        saxon1=random.choice(self.saxonArmy) # random name of the saxon
        viking1=random.choice(self.vikingArmy) # random name of the viking

        atack1 = saxon1.receiveDamage(viking1.attack()) # viking1.attack() == viking1.strength
     
        if saxon1.health <= 0:
            self.saxonArmy.remove(saxon1)

        return atack1 #saxon1.receiveDamage(viking1.strength)

    def saxonAttack(self):

        saxon2=random.choice(self.saxonArmy) # random name of the saxon
        viking2=random.choice(self.vikingArmy) # random name of the viking

        resultado_ataque2=viking2.receiveDamage(saxon2.attack()) # saxon2.attack() == saxon2.strength 
        
        if viking2.health <= 0:
            self.vikingArmy.remove(viking2)

        return resultado_ataque2 #viking2.receiveDamage(saxon2.strength)

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
