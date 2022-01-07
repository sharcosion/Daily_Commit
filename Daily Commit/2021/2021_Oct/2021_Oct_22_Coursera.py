# Tuple () are immutable, meaning you can't change once decided content.

Ratings = (10,9,10,8)

RatingSorted = sorted(Ratings)


NT = (1,2, ("pop","rock"))

NT[2]: ("pop", "rock")[1] = "rock"

NT[2][1] = "rock"


# List [] is mutable

L = [1,2,3]

L.extends(["new list item 1", 2])

# [1,2,3,"new list item 1", 2]

L.append["new list item 1", 2])

# [1,2,3,["new list item 1", 2]]

del(L[0])

"A,B,C,D".split(",")

# List clone

A = [1,2,3]
B = A[:] # Clone A to B  

# get help on list or tuple
help(A)