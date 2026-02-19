import numpy as np
matrix = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])

# there are two ways of finding the transpose
transpose_matrix1 = matrix.T 
transpose_matrix2 = np.transpose(matrix) 

print(transpose_matrix1)
print(transpose_matrix2)