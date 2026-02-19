import numpy as np

matA = np.array([
    [1, 2],
    [3, 4]
])

def adjoint_of_2by2(matrix2by2):
    a = matrix2by2[1][1]
    b = - matrix2by2[0][1]
    c = - matrix2by2[1][0]
    d = matrix2by2[0][0]
    
    adjoint_matrix = np.array([
        [a, b],
        [c, d]
    ])
    
    return adjoint_matrix

adjointA = adjoint_of_2by2(matA)
print(adjointA)
