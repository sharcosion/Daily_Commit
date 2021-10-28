df = pd.read_csv('data/data.csv', index_col=['Day'])
# To get Friday's temperature
>>> df.loc['Fri', 'Temperature']
10.51


# The equivalent `iloc` statement
>>> df.iloc[4, 1]
10.51


# Multiple rows
>>> df.loc[['Thu', 'Fri'], 'Temperature']
Day
Thu    14.44
Fri    10.51
Name: Temperature, dtype: float64
# Multiple columns
>>> df.loc['Fri', ['Temperature', 'Wind']]
Temperature    10.51
Wind              26
Name: Fri, dtype: object



>>> df.iloc[[3, 4], 1]
Day
Thu    14.44
Fri    10.51
Name: Temperature, dtype: float64
>>> df.iloc[4, [1, 2]]
Temperature    10.51
Wind              26
Name: Fri, dtype: object



# Slicing column labels
rows=['Thu', 'Fri']
df.loc[rows, 'Temperature':'Humidity' ]




# Slicing row labels
cols = ['Temperature', 'Wind']
df.loc['Mon':'Thu', cols]