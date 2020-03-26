#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
#import statements 
import math
import os 
import random
import sys



#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square=[e*e for e in range(21)]
print(square)


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two=[2**e for e in range (51)]
print (power_of_two)




#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
sqrt=[math.sqrt(e) for e in range(101)]
print(sqrt)


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
my_list=[e for e in range(-11,1)]
print(my_list)

#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odd_numbers = [i for i in range(2,101) if (i%2!=0 or i==2) and (i%3!=0 or i==3) and (i%5!=0 or i==5) and (i%7!=0 or i==7)]
print (odd_numbers)


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven=[e for e in range(1,1001) if e%7==0]
print(divisible_by_seven)



#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'

vowels=["a","e","i","o","u"]

non_vowels=[e for e in teststring if e not in vowels]
print(non_vowels)


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
sentence="The Quick Brown Fox Jumped Over The Lazy Dog"

capital_letters=[e for e in sentence if e.isupper() and e!=" "]
print(capital_letters)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

consonants=[e for e in sentence if e not in vowels]
print(consonants)



#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.



files = [f for f in sorted(os.listdir(/Users/julio/datamad0320))]
print(files)


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_list=[e for e in random.choices(range(0,101),k=10)]
print(random_list,random_list,random_list,random_list)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

flatten_list=[x for e in list_of_lists for x in e]
print(flatten_list)



#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats=[float(x) for e in list_of_lists for x in e]
print(floats)



#14. Handle the exception thrown by the code below by using try and except blocks. 


for i in ['a','b','c']:
    try:
        print (i**2)
    except Exception as err:
        print("err")
        break
    


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

try:
    z = x/y
except Exception as err:
    print("All done")
    print(err,type(err))



#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]

try:
    print(abc[3])
except Exception as err:
    print(err,type(err))




#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 


def division(a,b):
    if b==0:
        raise valueError("You should choose a different number")
    elif type(a)!=int or type(b)!=int:
        raise ValueError("Yoy should choose an int as a number")
    return a/b

while True:
    try:
        a= input("Pass a number: ")
        b = input("Pass other number: ")
        print(division())
        break
    except:
        print("Try again")



#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

***La resolución de este ejercicio lo he visto en internet. Independientemente de que no se me 
ejecuta, lo que no he entendido de este ejercicio es que esto se ejecutaría si le dieramos un 
archivo que esté en nuestro repositorio. Por lo que no veo el sentido del ejercicio***

try:
  f = open("testfile","r")
  f.write("Test write this")
except:
  print("Something went wrong")
finally:
  f.close()




#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
***Aquí me pasa lo mismo que el ejercicio anterior***


fp = open('myfile.txt')

try:
    line = f.readline()
    i = int(s.strip())
except:
    print("Something went wrong")
finally:
  f.close()


#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
try:
    linux_interaction()
except:
    print('Linux function was not executed')



# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.

***Este ejercicio no me sale. No entiendo porque cuando se ejecuta el try, debería de ejecutarse 
la raiz cuadrada pero no pasa. Siempre me sale "try again"***


while True:

    try:
        n=input("Choose a number: ")
        if type(n)!=int:
         raise ValueError("Yoy should choose an int as a number")
         print(math.square(n))
        break
    except:
        print("Try again")
    else:
        print("ok")
    




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results=[e for e in range(1,1001) for n in range(2,10) if e%n==0 ]
print(results)
