#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)
print(np.__config__)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a=np.random.rand(2,3,5)

#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b=np.ones((5,2,3))

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

#a and b arrays do have the same size 
print(np.size(a)==np.size(b))

#8. Are you able to add a and b? Why or why not?

#We are not able to add a and b, even if they have the same size (a.k.a the same number of elementos) because \
#they have differen dimensionality

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c=np.transpose(b, (1,2,0))


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d=a+c

#Now it works because a and c have the same dimensionality

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)

print(d)


#12. Multiply a and c. Assign the result to e.

e=a*c

#13. Does e equal to a? Why or why not?

#e is iqual to a because we are multiplying a elementwise with c, which is an array with only ones in it.
#That is, we are multiplying each element by 1


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max=np.max(d)
d_min=np.min(d)
d_mean=np.mean(d)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f=np.empty((2,3,5))


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
i=0
for x in f:
        j=0
        for y in x:
                k=0
                for z in y:
                        if d_mean>d[i][j][k]>d_min:
                                f[i][j][k]=25
                        elif d_max>d[i][j][k]>d_mean:
                                f[i][j][k]=75
                        elif d[i][j][k]==d_mean:
                                f[i][j][k]=50
                        elif d[i][j][k]==d_min:
                                f[i][j][k]=0
                        elif d[i][j][k]==d_max:
                                f[i][j][k]=100
                        k+=1
                j+=1
        i+=1




#17. Print d and f. Do you have your expected f?
print(d)

print(f)

#I do have the expected array


#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
#("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:

f=np.empty((2,3,5),dtype=str)
i=0
for x in f:
        j=0
        for y in x:
                k=0
                for z in y:
                        if d_mean>d[i][j][k]>d_min:
                                f[i][j][k]='B'
                        elif d_max>d[i][j][k]>d_mean:
                                f[i][j][k]='D'
                        elif d[i][j][k]==d_mean:
                                f[i][j][k]='C'
                        elif d[i][j][k]==d_min:
                                f[i][j][k]='A'
                        elif d[i][j][k]==d_max:
                                f[i][j][k]='E'
                        k+=1
                j+=1
        i+=1

print(f)


