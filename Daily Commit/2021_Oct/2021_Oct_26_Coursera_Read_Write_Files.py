import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)


# Download Example file


#!wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt


# Read the Example1.txt

example1 = "Example1.txt"
file1 = open(example1, "r")



# Print the path of file

file1.name

# Print the mode of file, either 'r' or 'w'

file1.mode

# Read the file

FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line

print(FileContent)

# Type of file content

type(FileContent)

# Close file after finish

file1.close()


"""
A Better Way to Open a File
Using the with statement is better practice, it automatically closes the file even if the code encounters an exception. The code will run everything in the indent block then close the file object.

"""
# Open file using with

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
    
    
# Verify if the file is closed

file1.closed

# Read first four characters

with open(example1, "r") as file1:
    print(file1.read(4))
    
    
# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
    
# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())
    
    
'''
We can also pass an argument to  readline()  to specify the number of charecters we want to read. However, unlike  read(),  readline() can only read one line at most.

'''

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1



# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()
    
# Each element of the list corresponds to a line of text:
# Print the first line

FileasList[0]


# Write line to file
exmp2 = '/resources/data/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
    
    
# Write lines to file

with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    
 
 

# Sample list of text

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines

# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        
        
# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    

# Write a new line to text file

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
    
    
# Verify if the new line is in the text file

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
"""
Additional modes
It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines. Luckily we can access the file in the following modes:

r+ : Reading and writing. Cannot truncate the file.
w+ : Writing and reading. Truncates the file.
a+ : Appending and Reading. Creates a new file, if none exists.

"""


'''
It is often very useful to know where the 'cursor' is in a file and be able to control it. The following methods allow us to do precisely this -

.tell() - returns the current position in bytes
.seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end

'''


with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )
    
    
with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())


# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())