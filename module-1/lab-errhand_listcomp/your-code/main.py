import math
import os
import random
import sys


#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.

list1=range(21)
square=[math.sqrt(e) for e in list1]
print(square)

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.

list2=range(51)
power_of_two=[2**e for e in list2]
print(power_of_two)

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.

list3=range(101)
sqrt=[math.sqrt(e) for e in list3]
print(sqrt)

#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.

list4=range(11)
my_list=[-e for e in list4]
my_list.reverse()
print(my_list)

#5. Find the odd numbers from 1-100. Use odds as the name of the list. 

list5=range(101)
odds=[e for e in list5 if e%2!=0]
print(odds)

#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.

list6=range(1001)
divisible_by_seven=[e for e in list6 if e%7==0]
print(divisible_by_seven)

#7. Remove all of the vowels in a string. 
#Hint: make a list of the non-vowels. Use non_vowels as the name of the list.

teststring1= 'Find all of the words in a string that are monosyllabic'
non_vowels=[c for c in teststring1 if c not in ('a','e','i','o','u')]
print(non_vowels)

#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  

teststring2='The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters=[c for c in teststring2 if c.isupper()==True]
print(capital_letters)

#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.

consonants=[c for c in teststring2 if c not in ['a','A','e','E','i','I','o','O','u','U']]
print(consonants)

#10. Find the folders you have in your datamad0320 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.

datamad0320=os.listdir("../../../") #Relative path de datamad0320 desde main.py
files=[os.listdir("../../../"+c) for c in datamad0320 if os.path.isdir("../../../"+c)==True]
print(files)

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module

random_lists=[[random.randint(0,100) for _ in range(10)] for _ in range(4)]
print(random_lists)

#12. Flatten the following list of lists. Use flatten_list as the name of the output.

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list=[elemento for lista in list_of_lists for elemento in lista]
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]
floats=[[float(num) for num in range(len(lista))] for lista in list_of_lists]
print(floats)

#14. Handle the exception thrown by the code below by using try and except blocks.
#Check in provided resources the type of error you may use. 

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("You cannot operate with string and int.")

#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
#Check in provided resources the type of error you may use. 

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Dividing by 0 not possible.")
finally:
    print("All done.")

#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    abc=[10,20,20]
    print(abc[3])
except IndexError:
    print("You are calling a number out of the index range.")

#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

try:
    [x,y] = input("Write two integers separated by a comma: ").split(',')
    print(int(x)/int(y))
except (ZeroDivisionError,ValueError):
    print("Dividing by 0 not possible.")

#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print("File not found.")

#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
#note: strip() returns a copy of the string with both leading and trailing characters removed

try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except (FileNotFoundError):
    print("File not found")
except (ValueError):
    print("Data cannot be convertable to int.")

#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except AssertionError:
    pass

# Bonus

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.

while True:
    try:
        num=input("Enter an integer: ")
        print(math.sqrt(int(num)))
        break
    except ValueError:
        print("Your input is not valid. Try again.")
    else: 
        pass

# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results=list(set([num for num in range(1001) for _ in range(2,10) if num % _ ==0]))
print(results)


# Bonus Bonus 

# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

try:
    Total_Marks = int(float(input("Enter Total Marks Scored: ")))
    Num_of_Sections = int(float(input("Enter Num of Sections: ")))
except MyError:
    print("The number of sections is less than 2.")

class MyError(ValueError):
    self

