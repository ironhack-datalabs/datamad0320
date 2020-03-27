
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health-=damage

"""
# Viking
class Viking:
    def __init__(self):

# Saxon
class Saxon:
    def __init__(self):

# War
class War:
    def __init__(self):
"""

#python3 vikingsClasses.py -v -k testSoldier