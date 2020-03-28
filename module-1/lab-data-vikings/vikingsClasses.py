# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    # Aquí van los métodos
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
       
    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    # Aquí van los métodos
    # Reimplementamos receiveDamage
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        if self.health <= 0:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"




        
  

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    # Aquí van los métodos
    # Reimplementamos receiveDamage
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        if self.health <= 0:
            return "A Saxon has died in combat"



    
    

# War

import random
class War:  
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    # Aquí van los métodos
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        # Sacar de forma aleatoria un sajón y un vikingo
        sajon = random.choice(self.saxonArmy)
        vikingo = random.choice(self.vikingArmy)

        resultado = sajon.receiveDamage(vikingo.attack())
        if sajon.health <= 0:
            self.saxonArmy.remove(sajon)
        return resultado

    def saxonAttack(self):
        # Sacar de forma aleatoria un sajón y un vikingo
        sajon = random.choice(self.saxonArmy)
        vikingo = random.choice(self.vikingArmy)
        resultado = vikingo.receiveDamage(sajon.attack())
        if vikingo.health <= 0:
            self.vikingArmy.remove(vikingo)
        return resultado
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."




