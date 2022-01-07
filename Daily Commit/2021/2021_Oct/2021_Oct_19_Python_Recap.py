'''
    A lambda function is a small anonymous function.

    A lambda function can take any number of arguments, but can only have one expression.

    Syntax
    lambda arguments : expression
    The expression is executed and the result is returned:
    

'''

# Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))



def myfunc(n):
    return lambda a : a * n
  

def myfunc(n):

    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



for x in cars:
    print(x)
    
    
cars.append("Honda")
cars.pop(1)
cars.remove("Volvo")


# Class 
class MyClass:
  x = 5
  
p1 = MyClass()
print(p1.x)


  
'''
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

'''
# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

'''
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''


# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

'''
Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

Example
Create a class named Student, which will inherit the properties and methods from the Person class:
'''
class Student(Person):
  pass
  
  
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

#Example
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear
    
    
    
'''
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''

#Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

'''

Create a Module
To create a module just save the code you want in a file with the file extension .py:

'''

# Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)
  

# Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")



# Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)

#Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)