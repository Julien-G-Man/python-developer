import numpy as np

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

if __name__ == "__main__":
    is_idempotent = isIdempotent(matA, matB)
    print(f"Is matrix A idempotent: {is_idempotent}")
