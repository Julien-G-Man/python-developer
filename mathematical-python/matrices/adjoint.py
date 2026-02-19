import numpy as np

matA = np.array([
    [1, 2],
    [3, 4]
])

def adjoint_of_2x2(matrix2by2):
    a = matrix2by2[1][1]
    b = - matrix2by2[0][1]
    c = - matrix2by2[1][0]
    d = matrix2by2[0][0]
    
    adjoint_matrix = np.array([
        [a, b],
        [c, d]
    ])
    
    return adjoint_matrix

if __name__ == "__main__":
    adjointA = adjoint_of_2x2(matA)
    print(adjointA)
