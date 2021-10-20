# Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# Python RegEx

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


'''
What is PIP?
PIP is a package manager for Python packages, or modules if you like.
'''



'''
Python Try Except

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''


#Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
  
#Else
#You can use the else keyword to define a block of code to be executed if no errors were raised:

#In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
  
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
#Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
  
# Raise an error and stop the program if x is lower than 0:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
  
  

#Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
  


'''
    User Input
'''

username = input("Enter username:")
print("Username is: " + username)


'''
String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
'''

# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#Format the price to be displayed as a number with two decimals:

txt = "The price is {:.2f} dollars"


myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


'''

What is NumPy?
NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python.

Why Use NumPy?
In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.


'''

'''
Why is NumPy Faster Than Lists?
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.


'''


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)


# Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

# output
#[1 2 3 4 5]
# <class 'numpy.ndarray'>

#Create an array with 5 dimensions and verify that it has 5 dimensions:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)




import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])
#7


'''
Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, where the row represents the dimension and the index represents the column.

'''

# Access the element on the first row, second column:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])



import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

#6

# Return every other element from the entire array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])


#[1 3 5 7]


'''
Data Types in Python
By default Python have these data types:

    strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
    integer - used to represent integer numbers. e.g. -1, -2, -3
    float - used to represent real numbers. e.g. 1.2, 42.42
    boolean - used to represent True or False.
    complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
'''


'''
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )

'''


#Checking the Data Type of an Array
#The NumPy array object has a property called dtype that returns the data type of the array:

#Example
#Get the data type of an array object:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)



'''
Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
'''

#Change data type from float to integer by using 'i' as parameter value:

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)


#NumPy Array Copy vs View

'''
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''
# Make a copy, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# Make a view, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


#Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.


# Print the shape of a 2-D array:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

# [[[[[1 2 3 4]]]]]
# shape of array : (1, 1, 1, 1, 4)



#Reshape From 1-D to 2-D
#Example
#Convert the following 1-D array with 12 elements into a 2-D array.

# The outermost dimension will have 4 arrays, each with 3 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
'''

[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

'''


# Convert the array into a 1D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)


print(newarr)




# Iterate on each scalar element of the 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
    
    
  
#Iterating Arrays Using nditer()
#The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.

#Iterating on Each Scalar Element
#In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.

# Iterate through the following 3-D array:

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
  
  
 