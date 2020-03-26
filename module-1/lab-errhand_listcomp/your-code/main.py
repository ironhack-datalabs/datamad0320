#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
import math
import random
import os
import sys

#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square =[e**2  for e in range(21)]
print (square)


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
e = 2
power_of_two= [e**c for c in range(50)]
print(power_of_two, len (power_of_two))



#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt= [c**2 for c in range(101)]
print(sqrt)


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list = [e for e in range(-10,1)]
print(my_list)



#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odds = [ e for e in range(1,100 ,2)]
print(odds)


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use  the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [e for e in range(1,1001) if e%7 ==0]
print(divisible_by_seven)


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels = [e for e in teststring  if len([i for i in e if i in ['a','e','i' ,'o', 'u']])  == 0 ]
print(non_vowels)




#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

setence = ('The Quick Brown Fox Jumped Over The Lazy Dog')
capital_letters =[e for e in setence if e.lower() == e]
print ( capital_letters)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

sentence = ('The quick brown fox jumped over the lazy dog')
consonants = [e for e in sentence  if len([i for i in e if i in ['a','e','i' ,'o', 'u']])  > 0 ]
print(consonants)



## NO SE POR QUE NO LEE EL ARCHIVO :(
#10. Find the folders you have in your datamad0320 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.
file_names = []
for file_name in os.listdir("datamad0320" ):
    file_path = os.path.join("datamad0320" , file_name)
    if os.path.isfile(file_path):
        file_names.append(file_name)
print(file_names)
files= [next(os.walk("datamad0320"), ([],[],[]))[2]]
print(files)

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_lists=[ e for e in random.choices(range(1,101), k=11 )]
print(random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list= [ l for s in list_of_lists for l in s ]
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats =[float(e) for d in list_of_lists for e in d]
print(floats)

#14. Handle the exception thrown by the code below by using try and except blocks. 

try:
    for i in ['a','b','c']:
        print i**2
        raise SyntaxError("ErrorSyntax")  
except SyntaxError:
    print(f"Falla en la sintaxix")
   

#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

try:
    x = 5
    y = 0
    z = x/y
    raise ZeroDivisionError("ZeroDivisionError")
except ZeroDivisionError:
    
    print (f"El error a arreglar es de indole ZeroDivisionError ")   
print(f'All Done')


#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
try:
    abc=[10,20,20]
    print(abc[3])
    raise IndexError("IndexErro")
except IndexError:
    print(f"Error de indice")



#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 
try:
    print (3/0) 
    raise ZeroDivisionError("ZeroDivisionErro")
except ZeroDivisionError:
    print(f"No se puede dividir por 0")


def saluda(nombre, edad):
    if type(edad) != int:
        raise ValueError("ValueError")
    if type(nombre) != str:
        raise ValueError("ValueError")
    return "Hola "+ nombre + " Tienes" + str(edad)

while True:
    try:
        name = input("Cual es su nombre ")
        age = input("Que edad tienes ")
        print(saluda(name,int(age)))
        
        break
    except ValueError:
        print("Lo siento, has metido un dato mal, intentalo de buevo")



#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
try:
    f = open('testfile','r')
    f.write('Test write this')
    raise FileNotFoundError(f"FileNotFoundError, don,t such file or directory f")
except FileNotFoundError:
    print(f"No encuentra los ficheros")


#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
try:
    fp = open('myfile.txt')
    raise NameError('FileNotFoundError')

except FileNotFoundError:       
    pass
try :
    line = f.readline()
    i = int(s.strip())
    raise NameError('IndentationError')
except NameError: 

    print("Bueno creo que lo tengo que areglar el fichero que no encuentra y el valor")    




#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 
try:
    def linux_interaction():
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
        print('Doing something.')
        raise IndentationError('IndentationError')
except IndentationError:
    print (f"no se por que no va el import sys")

# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.
def square(number):
    if type(number) != int:
        raise ValueError("You should pass number as an int")
        
    return f"The square of your number is  {number**2}"

while True:
    try:
        elija = input("Choose a number ")
        print(square(int(elija)))
        break
    except :
        print(F"Vuelve a intentarlo")


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results = [e for e in range(1,1000) for d in range(2,9) if e%d == 0]
print(set(results))


# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

#Total_Marks = int(input("Enter Total Marks Scored: ")) 
#Num_of_Sections = int(input("Enter Num of Sections: "))
