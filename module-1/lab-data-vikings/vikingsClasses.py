# Modules
import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        s = Soldier(self.health, self.strength)     #if we create a var, which include a class with each respective arguments
        return s.strength                           #now we can use the arguments without, self, as it is included in the var
                                                    #if the var was created out of the function, we could have use the arguments 
    def receiveDamage(self, damage):                #with the var "s" instead of "self."
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)          #when using super().__init__ the constructor is inheriting health and strenght from Soldier
        #self.health = health                       #that is why is not necessary to define them again
        #self.strength = strength
    """
    def attack(self):                               #the attack func comes also from Soldier, so there is no need to define again
        return self.strength
    """
    def receiveDamage(self, damage):
        self.health -= damage
        while self.health > 0:
            return self.name + f" has received {damage} points of damage"
        return self.name + f" has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        #self.health = health
        #self.strength = strength
    """
    def attack(self):
        return self.strength
    """
    def receiveDamage(self, damage):
        self.health -= damage
        while self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        return "A Saxon has died in combat"

    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        srd = saxon.receiveDamage(viking.attack())                  #here we use the function "attack()" which the same to say "viking.strength"                      
        if saxon.health < 1:                                        #here we have another example of the use of an argument with a var instead of self
            self.saxonArmy.remove(saxon)                            #why? saxon is a random saxon from saxonArmy which was append in addSaxon function,
        return srd                                                  #which also comes from a defined Saxon from the file "4-testWar.py" --> See line 34
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        vrd = viking.receiveDamage(saxon.attack())
        if viking.health < 1:
            self.vikingArmy.remove(viking)
        return vrd 

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    
    
    
