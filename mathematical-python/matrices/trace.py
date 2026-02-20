import numpy as np

matA = np.array([
    [1, 2],
    [3, 4]
])

matB = np.array([
    [2, -2, 1],
    [-1, 1, 0],
    [0, 0, -0]
])

def trace(matrix):
    if len(matrix) == 2:
       return matrix[0][0] + matrix[1][1]
    if len(matrix) == 3:
        return matrix[0][0] + matrix[1][1]  + matrix[2][2]
    
    
if __name__ == "__main__":
    print(f"The trace of matrix A is {trace(matA)}")
    print(f"The trace of matrix B is {trace(matB)}")