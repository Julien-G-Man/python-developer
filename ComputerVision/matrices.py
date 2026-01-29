"""
We use Numpy because:
- Vectorized operations
- Linear algebra support
- Same math as learned in theory
"""

import numpy as np

img = np.array([[0, 255, 1], 
                [120, 90, 50],
                [40, 12, 3]])

print("Original array\n", img)

# Element-wise subtraction
print("\nElement-wise subtraction\n", 255 - img)

# Shape awareness
print("\nShape awareness\n", img.shape)

# Data types matter
print("\nData type: ", img.dtype)

