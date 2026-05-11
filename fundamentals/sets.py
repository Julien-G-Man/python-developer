"""
A set is an immutable, unordered collection of unique elements that can consist of integers, floats, strings and tuples. 
However, sets cannot hold mutable elements such as lists, sets or dictionaries.
"""
import random

set1 = {'Jenny', 26, 'Parker', 10.5}
print(set1) # prints {10.5, 26, 'Jenny', 'Parker'}

# we can create sets from lists,all duplicates will vanish

list1 = [1, 2, 4, 8,6, 2, 3, 1]
set2 = set(list1)
print(set2)

# we use in to check if elements exist in the set
print(5 in set2) # returns bool

# built-in methods
name1 = "Julien"
set1.add(name1)
print(f"Adding {name1}")
print(set1)

name2 = random.choice(list(set1))
set1.remove(name2)
print(f"Removing {name2}")
print(set1)