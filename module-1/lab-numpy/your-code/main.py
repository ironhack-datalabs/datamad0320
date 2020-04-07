#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)

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

print(a.shape == b.shape)

#8. Are you able to add a and b? Why or why not?

print('It is not possible because they don\'t have the same structure')

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c=np.transpose(b, (1, 2, 0))
print(c.shape)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d=np.add(a,c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)
print('They have the same structure now')

#12. Multiply a and c. Assign the result to e.

e=np.multiply(a,c)
print(e)

#13. Does e equal to a? Why or why not?

print(np.array_equal(e,a))
print('')

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max=np.max(d)
d_min=np.min(d)
d_mean=np.mean(d)

#Now we want to label the values in d. 

#15. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f=np.empty([2,3,5])

#16. Populate the values in f.
#If a value in d is larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
#If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
#If a value equals to d_mean, assign 50 to the corresponding value in f.
#Assign 0 to the corresponding value(s) in f for d_min in d.
#Assign 100 to the corresponding value(s) in f for d_max in d.
#In the end, f should have only the following values: 0, 25, 50, 75, and 100.
#Note: you don't have to use Numpy in this question.

for i in range(d.shape[0]):
        for j in range(d.shape[1]):
                for k in range(d.shape[2]):
                        if (d[i][j][k]>d_min) and (d[i][j][k]<d_mean):
                                f[i][j][k]=int(25)
                        elif (d[i][j][k]>d_mean) and (d[i][j][k]<d_max):
                                f[i,j,k]=int(75)
                        elif d[i][j][k] == d_mean:
                                f[i][j][k]=int(50)
                        elif d[i][j][k] == d_min:
                                f[i][j][k]=int(0)
                        elif d[i][j][k] == d_max:
                                f[i][j][k]=int(100)
                
        
#17. Print d and f. Do you have your expected f?

print(d)
print(f)

#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
#("A", "B", "C", "D", and "E") to label the array elements? 

labels={0:'A', 25:'B', 50:'C', 75:'D', 100:'D'}

f_lab=np.empty([2,3,5],dtype=str)

for i in range(f.shape[0]):
        for j in range(f.shape[1]):
                for k in range(f.shape[2]):
                        f_lab[i][j][k]=labels[f[i][j][k]]
                      
print(f_lab)