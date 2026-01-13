"""
Numpy is the foundation for numerical operations in Python.
It provides fast arrays and math functions.
"""

import numpy as np
import random

arr = np.array([1, 2, 3])
print(arr * 2)

# a 3x3 matrix of random integers from 1-10
matrix = np.random.randint(1, 11, size=(3, 3))
print(matrix)