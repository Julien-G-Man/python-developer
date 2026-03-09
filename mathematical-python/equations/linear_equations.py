import numpy as np

# Given Ax = B
matA = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

vectorA = np.array([2, 4, 6])

transformationB = matA * vectorA

print(transformationB)
