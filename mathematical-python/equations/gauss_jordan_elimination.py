import numpy as np

def gauss_jordan(A, b):
    # Form the augmented matrix
    n = len(b)
    aug = np.hstack([A, b.reshape(-1,1)])
    
    for i in range(n):
        # Make pivot = 1
        pivot = aug[i, i]
        aug[i] = aug[i] / pivot
        
        # Eliminate other entries in column i
        for j in range(n):
            if j != i:
                factor = aug[j, i]
                aug[j] = aug[j] - factor * aug[i]
    
    return aug

# Example system:
# ax1 + bx2 + cx3 = p
# dx1 + ex2 + fx3 = q
# gx1 + hx2 + ix3 = r

a, b, c = 1, 2, 1
d, e, f = 4, 1, 6
g, h, i = 7, 8, 5

A = np.array([[a, b, c],
              [d, e,f],
              [g, h, i]], dtype=float)

b = np.array([1, 6, 4], dtype=float)

if __name__ == "__main__":
    solution_matrix = gauss_jordan(A, b)
    print("RREF form:\n", solution_matrix)

    # Extract solution
    x = solution_matrix[:, -1]
    print("Solution: x1 = {:.2f}, x2 = {:.2f}, x3 = {:.2f}".format(*x))
