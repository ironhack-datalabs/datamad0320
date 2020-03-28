import random
import copy

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        oldHealth = self.health
        self.health = oldHealth - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return f'Odin Owns You All!'
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'

    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.viking = Viking
        self.vikingArmy.append(self.viking)

    def addSaxon(self, Saxon):
        self.saxon = Saxon
        self.saxonArmy.append(self.saxon)

    def vikingAttack(self):
        oldSaxonArmy = copy.deepcopy(self.saxonArmy)
        saxon_choice = random.choice(self.saxonArmy)
        viking_choice = random.choice(self.vikingArmy)
        clash = saxon_choice.receiveDamage(viking_choice.attack())
        for i in range(len(self.saxonArmy)):
            if self.saxon.health <= 0:
                self.saxonArmy = oldSaxonArmy.remove(oldSaxonArmy[i])
        if self.saxonArmy == None:
            self.saxonArmy = []
        return clash

    def saxonAttack(self):
        oldVikingArmy = copy.deepcopy(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        clash = viking.receiveDamage(saxon.attack())
        for i in range(len(self.vikingArmy)):
            if self.viking.health <= 0:
                self.vikingArmy = oldVikingArmy.remove(oldVikingArmy[i])
        if self.vikingArmy == None:
            self.vikingArmy = []
        return clash

    def showStatus(self):
        if ((len(self.saxonArmy) > 0) & (len(self.vikingArmy) > 0)):
            return "Vikings and Saxons are still in the thick of battle."
        elif (len(self.saxonArmy) == 0):
            return "Vikings have won the war of the century!"
        elif (len(self.vikingArmy) == 0):
            return "Saxons have fought for their lives and survive another day..."
            