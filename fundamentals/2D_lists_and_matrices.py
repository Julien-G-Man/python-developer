# 2D lists and matrices in Python

import numpy as np
# Example of a 3x3 matrix
matrix = [
    [4, 2, 8],
    [1, 5, 6], 
    [7, 1 ,5]
]

print(matrix[1][2])  # Access element at row 0, column 1 (output: 2)
det = np.linalg.det(matrix)
print(f"Determinant: {det}")

for matrices in matrix:
    for row in matrix:
        print(row)

    

