
#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
import math
import os
import random
import sys



#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [e**2 for e in range(1,20+1)]
print("Ejercicio 1:\n", square)



#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
power_of_two = [2**e for e in range(50)]
print("Ejercicio 2:\n", power_of_two)



#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt = [math.sqrt(e) for e in range(1,100+1)]
print("Ejercicio 3:\n", sqrt)



#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
my_list = sorted([-e for e in range(10+1)])
print("Ejercicio 4:\n", my_list)



#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
odds = [e for e in range(1,101) if e % 2 != 0]
print("Ejercicio 5:\n", odds)



#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [e for e in range(1,1001) if e % 7 == 0]
print("Ejercicio 6: \n", divisible_by_seven)


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels = [e for e in teststring if e not in ["a", "e", "i", "o", "u"]]
print("Ejercicio 7:\n", non_vowels)




#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
sentence = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = [e for e in sentence if e.isupper()]
print("Ejercicio 8:\n", capital_letters)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
sentence = 'The quick brown fox jumped over the lazy dog'
consonants = [e for e in sentence if e not in ["a", "e", "i", "o", "u", " "]]
print("Ejercicio 9: \n", consonants)



#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

# Establecer el path de mi repo
path = "/home/lee/Documentos/IRONHACK/LABS/datamad0320/"
files = [ item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
print("Ejercicio 10: \n",files)

# FUENTE: https://stackoverflow.com/questions/29206384/python-folder-names-in-the-directory

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_lists = [random.sample(range(101), 10) for e in range(4)]
print("Ejercicio 11: \n", random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [e for sublista in list_of_lists for e in sublista]
print("Ejercicio 12: \n", flatten_list)




#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [float(e) for sublista in list_of_lists for e in sublista]
print("Ejercicio 13: \n", floats)


#14. Handle the exception thrown by the code below by using try and except blocks. 
print("Ejercicio 14:")
try:
    for i in ['a','b','c']:
        print (i**2)
except Exception as error:
    # Mostrar el error por consola
    print(error, type(error))



#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 
print("Ejercicio 15:")
try:
    x = 5
    y = 0
    z = x/y
except Exception as error:
    print("ERROR!!! --> ", error)



#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("Ejercicio 16:")
try:
    abc=[10,20,20]
    print(abc[3])
except Exception as error:
    print("ERROR!!! --> ", error)


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 
print("Ejercicio 17:")
# He creado una función que hace la división entre dos valores y 
# que me muestre error si alguno de los valores no es un integer o float, y si alguno es 0

def dividir(x, y):
    if (type(x) != (int or float)) and (type(y) != (int or float)):
        raise ValueError("Debes introducir un número (entero o decimal)")
    if x == 0 or y == 0 :
        raise ValueError("Tu número debe ser distinto de 0, so lerdx")
    return x/y

x = 5
y = 2

dividir(x,y)



#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("Ejercicio 18:")
try:
    f = open('testfile','r')
except Exception as error: 
    print("ERROR!!! --> ", error)
try:
    f.write('Test write this')
except Exception as error:
     print("ERROR!!! --> ", error)




#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
print("Ejercicio 19:")
try:
    fp = open('myfile.txt')
except Exception as error: 
    print(error)
try:
    line = f.readline()
except Exception as error: 
    print(error)
try:    
    i = int(s.strip())
# Meto en except el error por no existir la variable 'NameError'
# y el error de que el valor no se peuda convertir en integer 'ValueError'
except(NameError, ValueError):
    print('No está definida la variable i. La variable s no puede ser convertida a integer')




#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    try:
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
    except:
        print('Doing something.')
    
print("Ejercicio 20:\n", linux_interaction())


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 
results = [i for i in range(1,1001) if (i%j==0 for j in range(2,10))]
print("Ejercicio 22: \n", results)


# NEINN!!! NEEINN! NEEEIN!!!
# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))


