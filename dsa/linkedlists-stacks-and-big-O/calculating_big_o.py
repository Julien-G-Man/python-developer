colours = ['green', 'yellow', 'blue', 'pink', 'black', 'white', 'purple'] # O(1)
other_colours = ['orange', 'brown'] # O(1)

def complex_algorithm(colours, other_colours):
    colour_count = 0          # O(1)
    
    for colour in colours:
        print(colour)         # O(n)
        colour_count += 1     # O(n)
        
    for other in other_colours:
        print(other)          # O(m)
        colour_count += 1     # O(m)
        
    print(colour_count)       # O(1)
    
complex_algorithm(colours, other_colours) # O(4 + 2n + 2m)

"""
Simplifying Big O Notation
  1. Remove constants
    - O(4 + 2n + 2m) -> O(n + m)
  2. Differentiate variables for different inputs
    - O(n + m)
  1. Remove smaller terms
    - O(n + n^2) -> O(n^2)
"""
