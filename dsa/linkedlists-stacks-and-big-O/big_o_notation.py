"""
Big O notation describes how an algorithm's time or space usage grows as input size increases.
It helps compare efficiency and understand scalability.
"""

colours = ['green', 'yellow', 'blue', 'pink']

# O(1)
def constant(colours):
    print(colours[2])

print("==== Constant O(1) ====")
constant(colours)

# o(n), number of operation depend on 
# the number of elements in the list
def linear(colours):
    for col in colours:
        print(col) # O(4)

print("\n==== Linear O(n) ====") 
print("1 operation everytime")  
linear(colours)


# O(n^2)
def quadratic(colours):
    for first in colours:
        for second in colours:
            print(first, second)

print("\n==== Quadratic O(n^2) ====")
print("n=3: (3 * 3) = 9 operations")
quadratic(colours)


# O(n^3)
def cubic(colours):
    for first in colours:
        for second in colours:
            for third in colours:
                print(first, second, third)
print("\n==== Cubic O(n^3) ====")
print("n=3: (3 * 3 * 3) = 27 operations")
cubic(colours)