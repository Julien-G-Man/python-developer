"""
Hash tables are data structures that use a hash function to map keys to values.
Basic operations: insert, lookup, and delete — all average O(1).
Handle collisions via chaining or open addressing.
Common uses: dictionaries, caching, fast lookups, and indexing.

Python hashtables are dictionaries
"""

menu = {
    'lasanga': 15.4,
    'mousaka': 21.35,
    'sushi': 16.4
}

print(menu.get('lasanga'))
print(list(menu.items()))
print(list(menu.keys()))
print(list(menu.values()))

# iterate
for key, value in menu.items():
    print(key, value)

# remove key-value pair
del menu['mousaka']

# empty dictionary
menu.clear()

# delete dictionary completely
del menu