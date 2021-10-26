# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)



# Build-in function print()

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)


# Use sum() to add every element in a list or tuple together

sum(album_ratings)

# Show the length of the list or tuple

len(album_ratings)



# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)
        

# Implement the printlist function

PrintList(['1', 1, 'the man', "abc"])


"""
Setting default argument values in your custom functions
You can set a default value for arguments in your function. For example, in the isGoodRating() function, what if we wanted to create a threshold for what we consider to be a good rating? Perhaps by default, we should have a default rating of 4:

"""

# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)


# Test the value with default value and with input

isGoodRating()
isGoodRating(10)

'''
Collections and Functions
When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:
'''

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
    
    
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
    
    
    




