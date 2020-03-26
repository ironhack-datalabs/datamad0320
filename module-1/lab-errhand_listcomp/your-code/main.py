#Example: 
"""
eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)
"""
#Insert here the module/library import statements 
#import math
#from os import listdir
#from os.path import isdir, join
#import random
#import sys

"""
#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square=[i**2 for i in range(20)]
print(square)




#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two=[2**i for i in range(50)]
print(power_of_two)




#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt= [math.sqrt(i) for i in range(100)]
print(sqrt)




#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list=[i for i in range(-10,1)]
print(my_list)




#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odds=[i for i in range(1, 101) if i%2!=0]
print(odds)




#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven=[i for i in range(1, 10001) if i%7==0]
print(divisible_by_seven)




#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'

vowels=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
non_vowels=[letter for letter in teststring if letter not in vowels]
print(*non_vowels)




#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

sentence='The Quick Brown Fox Jumped Over The Lazy Dog'

capital_letters=[letter for letter in sentence if letter.isupper()]
print(capital_letters)




#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

vowels=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
sentence='The quick brown fox jumped over the lazy dog'
consonants=[letter for letter in sentence if letter not in vowels + [' ']]
print(consonants)




#10. Find the folders you have in your datamad0320 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

#path='/home/b/datamad0320'
path='../../../' #equivale a datamad0320/module-1/lab-errhand_listcomp/you-code, 
                 #desde el punto de vista de la carpeta donde está el main.py
files=[f for f in listdir(path) if isdir(join(path, f))]
print(files)




#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_lists=[random.sample(range(101), 10) for i in range(4)]
print(random_lists)




#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

flatten_list=[e for ls in list_of_lists for e in ls]
print(flatten_list)




#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats=[[float(e) for e in ls ]for ls in list_of_lists] #Without flattening
#floats=[float(e) for e in ls for ls in list_of_lists] #Flattening the list
print(floats)




#14. Handle the exception thrown by the code below by using try and except blocks. 

# esta intentando sacar el cuadrado de un string
for i in ['a','b','c']:
    try:
        print (i**2)
    except Exception as error:
        print('Please, introduce a number') 
    



#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError as error:
    print('Please, do not enter zero as divider')
finally:
    print('All Done')




#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]

try:
    print(abc[3])
except IndexError as error:
    print('Index division out of range')




#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

# REPASAR ESTA!!!
def division (numbers):
    num=[]
    for i in numbers:
        try:
            num += [int(i)]
        except: # If error, nothing happens and it skips to the following element
            pass
            
    if len(num)!= 2: 
        raise IndexError('Please, insert two numbers')
    if num[1]==0:
        raise ZeroDivisionError('Please, enter a non-zero divider')
    if len(num)==2 and num[1]!=0:
        print('result:', num[0]/num[1])   

numbers=input('Please, provide a couple of numbers ')
division(numbers)




#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError as error:
    print('This file is not in this directory')




#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('myfile.txt')
except FileNotFoundError: 
    print ('File does not exist')
line = fp.readline()
try:
    i = int(line.strip())
except ValueError:
    print('Data cannot be converted into integer')




#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except OSError:
    print ('This function only runs in Linux systems')




# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.


while True:
    try:
        number=input('Please, enter a number:')
        print((int(number))**2)
        break
    except ValueError:
        print('Data is not correct. Please, try again')




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results=[x  for x in range(1, 1001) for i in range(2,10) if x%i==0]
results=set(results)
print(results)



# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

class MyError (Exception): # MyError is subclass of Exception error
    # The class needs the method __init__ to initiate the error
    def __init__(self, message): #When we call the error, we can add a message 
        self.message = message

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))
if Num_of_Sections <2:
    raise MyError('Number of sections should be equal or greater than 2')
"""

