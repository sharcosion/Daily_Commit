"""
Run each piece of code and observe the exception raised

1/0
ZeroDivisionError occurs when you try to divide by zero.

y = a + 5
NameError -- in this case, it means that you tried to use the variable a when it was not defined.

a = [1, 2, 3]
a[10]
IndexError -- in this case, it occured because you tried to access data from a list using an index that does not exist for this list.
There are many more exceptions that are built into Python, here is a list of them 

https://docs.python.org/3/library/exceptions.html
"""



try:
    # code to try to execute
except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")


# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
    
# code that will execute if there is no exception or a one that we are handling


# potential code before try catch

try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling


 a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")