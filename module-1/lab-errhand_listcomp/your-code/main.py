#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]



#Insert here the module/library import statements 

import math
import os
import random
import sys
"""
#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square=[e**2 for e in range(1,21)]




#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two=[e**2 for e in range(1,51)]




#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt=[(math.sqrt(50))]


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list=[e for e in range(-10,1)]




#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
odds=[e for e in range(1,101)if e%2==1]







#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven=[e for e in range(1,1001) if e%7==0]




#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'

vowels= "a","e","o","i","u"

non_vowels=[e for e in teststring if e not in vowels]




#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
sent='The Quick Brown Fox Jumped Over The Lazy Dog'

c_l="ABCDEFGHIJKLMNOPQRSTU,W,X,Y,Z"

capital_letters=[e for e in sent if e in c_l]





#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
z='The quick brown fox jumped over the lazy dog'
z_1="bcdfghjklmnpqrstvwxyz"

consonants=[e for e in z if e in z_1]




#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

# pack userclara/desktop/.. en vez rutas relativas con * user buscame en todas las carpetas...
#3 funciones a utilizar ,file con condicional

files = [ item for item in os.listdir("/Users/albertjoselobera/datamad0320") if os.path.isdir(os.path.join("/Users/albertjoselobera/datamad0320", item)) ]



#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results


random_lists=[[e for e in random.choices(range(1,101),k=10)],[e for e in random.choices(range(1,101),k=10)],[e for e in random.choices(range(1,101),k=10)],[e for e in random.choices(range(1,101),k=10)]]





#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

flat_list = [x for e in list_of_lists for x in e]




#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats=[float(x) for e in list_of_lists for x in e ]






#14. Handle the exception thrown by the code below by using try and except blocks. 


for i in ['a','b','c']:
    try:
        print (i**2)
    except Exception as error:
        
        break
    

#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0
try:
    z = x/y
except Exception as error:
    print("Can´t devide by 0")
finally:
    print("All done")





#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

    abc=[10,20,20]
try:
    print(abc[3])
except Exception as error:
    # print(type(error))



#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 


    #uno=int(input("number1: "))
    #dos=int(input("number2: "))

#def divide(uno,dos):
    #if uno != int:
    #raise V=alueError("You should pass number as an int")
    #if dos = int:
    #raise ValueError("You should pass number as an int")
    #x=uno/dos
    #return print(int(x))

# divide(uno,dos)



#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
try:
    f = open('testfile','r')

    f.write('Test write this')
    
except Exception as error:
    print(type(error))



#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
try:
    fp = open('myfile.txt')

    line = f.readline()
    i = int(s.strip())
except Exception as error:
    print("Check if: the file could not exist and the data could not be convertable to int")



#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    try:
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
        print('Doing something.')
    except Exception as e:
        


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.


def asking(beep):
    
    if type(beep) != int:
        raise ValueError("You should type it as an int")

    x=beep**2
    return f"Number  {beep}"


    while True:
        try:
            beep=input("Write  an integer number: ")
            break
            
        except: 
            print("Introduce solo un numero int")
    
        
            
    







# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results=[e for e in range(1,1001)if e != e%2==0 and  e%9==1]



"""
# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python


Num_of_Sections=0

while Num_of_Sections <2:
    try: 
        Total_Marks = int(input("Enter Total Marks Scored: ")) 


        Num_of_Sections = int(input("Enter Num of Sections: "))


    except Exception as e:
        Print("Accepted calues, Num_of_Setions less than 2")






