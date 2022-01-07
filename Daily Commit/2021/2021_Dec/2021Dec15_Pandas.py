import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print('---------------')
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

print(myvar[0])


myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar["y"])


print('---------------')

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 


#refer to the row index:
print(df.loc[0])

# Note: This example returns a Pandas Series.

#use a list of indexes:
print(df.loc[[0, 1]])
#Note: When using [], the result is a Pandas DataFrame.

# adding index names 
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#refer to the named index:
print(df.loc["day2"])


print('---------------')

df = pd.read_csv('data.csv')

print(df.to_string()) 
print(df) 
print(pd.options.display.max_rows) 

pd.options.display.max_rows = 9999

print(df) 

print('---------------')

df = pd.read_json('C:/Users/User/OneDrive/Daily Study/data.json')

print(df.to_string()) 


'''
JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

'''

'''

Viewing the Data
One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top.
'''
print('---------------')

df = pd.read_csv('data.csv')

print(df.head(10))

print(df.tail()) 

# The DataFrames object has a method called info(), that gives you more information about the data set.

print(df.info()) 


#Return a new Data Frame with no empty cells:
print('---------------')

df = pd.read_csv('dirtydata.csv')

new_df = df.dropna()

print(new_df.to_string())

#Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# If you want to change the original DataFrame, use the inplace = True argument:


df.dropna(inplace = True)

print(df.to_string())

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.


'''
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:

'''

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

# Replace NULL values in the "Calories" columns with the number 130:


df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)



'''
Let's try to convert all cells in the 'Date' column into dates.

Pandas has a to_datetime() method for this:
'''

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())



print(df.duplicated())

df.drop_duplicates(inplace = True)
# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

