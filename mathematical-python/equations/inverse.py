import numpy as np

# Note that the solution is
# [ A|I ] --> [ I|A^-1 ] 

def gauss_jordan_inverse(A):
    n = A.shape[0]
    # Augment A with the identity matrix
    aug = np.hstack([A.astype(float), np.identity(n)])
    
    for i in range(n):
        # Make pivot = 1
        pivot = aug[i, i]
        if pivot == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        aug[i] = aug[i] / pivot
        
        # Eliminate other entries in column i
        for j in range(n):
            if j != i:
                factor = aug[j, i]
                aug[j] = aug[j] - factor * aug[i]
    
    # The right half of aug is now the inverse
    return aug[:, n:]

# Example matrix
A = np.array([[2, 3, 1],
              [4, 1, 2],
              [1, 2, 3]])

A_inv = gauss_jordan_inverse(A)

if __name__ == "__main__":
    print("Inverse of A:\n", A_inv)

    # Verify: A * A_inv should be identity
    check = np.dot(A, A_inv)
    check_clean = np.round(check, decimals=10)
    print("\nCheck (A * A_inv):\n", check_clean)
