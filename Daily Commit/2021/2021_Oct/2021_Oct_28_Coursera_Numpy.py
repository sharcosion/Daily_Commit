# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
%matplotlib inline  

# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    
    
    
# Create a python list

a = ["0", 1, "two", "3", 4]



# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])



"""
What is numpy
A numpy array is similar to a list. It's usually fixed in size and each element is of the same type. We can cast a list to a numpy array by first importing numpy:
"""

# import numpy library

import numpy as np 


# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])



# Check the type of the array

type(a)


# Create a numpy array

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# Check the type of array

type(b)

# Assign the first element to 100

c[0] = 100
c

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# Get the number of dimensions of numpy array

a.ndim



# Get the shape/size of numpy array

a.shape


# Create a numpy array

a = np.array([1, -1, 1, -1])


# Get the mean of numpy array

mean = a.mean()
mean


# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation


# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
b


# Get the biggest value in the numpy array

max_b = b.max()
max_b

# Get the smallest value in the numpy array

min_b = b.min()
min_b

u = np.array([1, 0])
u

v = np.array([0, 1])
v


# Numpy Array Addition

z = u + v
z




# Plot numpy arrays

Plotvec1(u, z, v)



# The value of pi

np.pi

# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])


"""
Linspace
A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers over a specified interval. We specify the starting point of the sequence and the ending point of the sequence. The parameter "num" indicates the Number of samples to generate, in this case 5:
"""


# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)



# We can use the function linspace to generate 100 evenly spaced samples from the interval 0 to 2π:
# Make a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)
# Make a numpy array within [0, 2π] and 100 elements 


#Convert the list [1, 0] and [0, 1] to numpy arrays a and b. Then, plot the arrays as vectors using the function Plotvec2 and find their dot product:

a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))