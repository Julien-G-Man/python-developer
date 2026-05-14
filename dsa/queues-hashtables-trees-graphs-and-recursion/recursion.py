"""
Recursion: a function that calls itself to solve smaller subproblems.
Key parts: a base case to stop recursion and a recursive step that reduces problem size.
Common uses: divide-and-conquer algorithms, tree/graph traversals, and combinatorics.
Be mindful of recursion depth and prefer iterative solutions or tail recursion optimizations when needed.
"""

from math import factorial as inbuilt_factorial

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def factorial_recursion(n):
    if n <= 1: return 1
    return n * factorial_recursion(n-1)


def fibonacci(n):
  if n <= 1:
        return n
  return fibonacci(n-1) + fibonacci(n-2)
    
    
# using dynamic programming, saving the solutions of 
# the subproblems in the cache variable.
cache = [None]*(100)

def dynamic_fibonacci(n):
    if n <= 1:
        return n
    
    # Check if the value exists
    if not cache[n]:
        # Save the result in cache
        cache[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
    
    return cache[n]
    

m = 6
print(inbuilt_factorial(m))
print(factorial(m))
print(factorial_recursion(m))
print(fibonacci(m))
print(dynamic_fibonacci(m))