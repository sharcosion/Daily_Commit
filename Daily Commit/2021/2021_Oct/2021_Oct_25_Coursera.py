# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict

# Access to the value by the key

Dict["key1"]

# Access to the value by the key

Dict[(0, 1)]

# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


# Get value by keys

release_year_dict['Thriller'] 




# Get all the keys in dictionary

release_year_dict.keys() 


# Get all the values in dictionary

release_year_dict.values() 


# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict


# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict

album_sales_dict = {"The Bodyguard":50, "Back in Black":50, "Thriller":65}



# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1

# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set

# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A

# Add element to set

A.add("NSYNC")
A

# Remove the element from set

A.remove("NSYNC")
A

# Verify if the element is in the set

"AC/DC" in A

# Find the intersections

intersection = album_set1 & album_set2
intersection


# Find the difference in set1 but not set2

album_set1.difference(album_set2)  

# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)   

# Find the union of two sets

album_set1.union(album_set2)

# Check if superset

set(album_set1).issuperset(album_set2)   

# Check if subset

set(album_set2).issubset(album_set1)     