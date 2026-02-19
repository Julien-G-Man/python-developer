"""
Numpy is the foundation for numerical operations in Python.
It provides fast arrays and math functions.
"""

import numpy as np
import random


def isIdempotent(matA, matB):
    firstMult = matA * matB
    secondMult = matA * firstMult
    
    if firstMult.all() == secondMult.all():
        return True
    return False
   
matA = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

matB = np.array([
    [2, -2, 1],
    [-1, 1, 0],
    [0, 0, -0]
]) 

print(f"Is matrix A idempotent: {isIdempotent(matA, matB)}")

# a 3x3 matrix of random integers from 1-10
matrix = np.random.randint(1, 11, size=(3, 3))
# print(matrix)