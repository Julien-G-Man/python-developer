import numpy as np
from adjoint import adjoint_of_2x2
from idempotency import isIdempotent
from trace import trace

matA = np.array([
    [2, 5],
    [0, 1]
])

def inverse_of_2x2(matrix_2x2):
    det = np.linalg.det(matrix_2x2)
    inverse = (1 / det ) * (adjoint_of_2x2(matrix_2x2))
    return inverse

if __name__ == "__main__":
    print(f"Original matrix: \n{matA}")
    
    inverse_matrixA = inverse_of_2x2(matA)
    print(f"\nThe inverse matrix: \n{inverse_matrixA}")
    
    is_idempotent = isIdempotent(matA, inverse_matrixA)
    print(f"\nThe matrix is idempotent: {is_idempotent}")
    
    print(f"\nThe trace of matrix A is {trace(matA)}")
