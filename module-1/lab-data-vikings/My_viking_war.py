from vikingsClasses import Soldier, Viking, Saxon, War
import random
import time

##FUNCIÓN PARA GENERAR LOS EJÉRCITOS DE SAXONES Y VIKINGOS Y DEVUELVE UN OBJETO DE TIPO WAR:

def armies(n):
    def generateViking():
        #Some Norwegian names:
        name = random.choice(['Harald', 'Olaf', 'Bjorn', 'Hakon', 'Morten', 'Torstain', 'Torfin', 'Svein', 'Ole', 'Mona', 'Kaja', 'Eivind', 'Knut', 'Greta'])
        #Random strength and health
        strength = random.choice(range(80, 200))
        health = random.choice(range(200,300))
        return Viking(name=name, health=health, strength=strength)

    def generateSaxon():
        #Saxons are a bit worse than Vikings
        health = random.choice(range(180,280))
        strength = random.choice(range(60, 170))
        return Saxon(health=health, strength=strength)

    war_object = War()
    for e in range(n):
        viking = generateViking()
        saxon = generateSaxon()
        war_object.addSaxon(saxon)
        war_object.addViking(viking)
    return war_object


##INPUT DEL USUARIO PARA LA FUNCION, SOLO INTEGERS ENTRE 1 Y 10, Y LLAMAMOS A LA FUNCIÓN.
while True:
    try:
        #Solo entre 1 y 10 soldados, de otra manera se hace demasiado largo...
        n = int(input('Cuantos soldados por ejército?(1:10): '))
        if n<11 and n>0:
            break
        else: print("Must be an integer between 1 and 10")
    except ValueError:
        print("You have to input an integer between 1 and 10")

war = armies(n)


##CODIGO PARA SEGUIR LA BATALLA HASTA QUE UNO DE LOS DOS EJERCITOS NO TENGA SOLDADOS:
while len(war.saxonArmy) > 0 and len(war.vikingArmy) > 0:

    #Como va el combate:
    print(f"\n {len(war.vikingArmy)} vikings against {len(war.saxonArmy)} saxons")

    #Batalla:
    #Los turnos de combate van a ser al azar también!! 
    turn = random.choice(['s', 'v'])
    if turn == 's':
        s = war.saxonAttack()
        print(s)
    else:
        v = war.vikingAttack()
        print(v)
    print(war.showStatus())
    #Pause the program to give the user some time to read the imput
    time.sleep(2)

#Imprime el resultado de la batalla:
if len(war.saxonArmy) == 0:
    if len(war.vikingArmy) != n:
        print(f"\tbut Saxons only left {len(war.vikingArmy)} of them alive")
    else: print("\t and with no casualties!!")
elif len(war.vikingArmy)==0:
    if len(war.saxonArmy) != n:
        print(f"\tbut Vikings only left {len(war.saxonArmy)} of them alive")
    else: print("\t and with no casualties!!")

