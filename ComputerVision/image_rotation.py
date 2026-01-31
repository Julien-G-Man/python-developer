"""
An image is a grid of points.
For a pixel at row i, column j, we treat it as a point:
    [x, 𝑦]

Convention (important):
    x → column (horizontal)
    y → row (vertical)

So pixel (row, col) → (x = col, y = row)

Every geometric manipulation is:
    -> take a point → multiply by a matrix → get a new point

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("images/pascal.jpg").convert("RGB")
img_arr = np.array(img)
H, W, C = img_arr.shape

"""
At this point:
- img_arr[y, x] is a pixel
- (x, y) is a coordinate
"""

# Transformation matrices
def translation_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

# Rotation matrix (about origin)
def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])

# scaling matrix
def scaling_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

# Rotation about image center (critical)
# image center:
cx = W / 2
cy = H / 2
theta = 135 # 180°

# Translate → rotate → translate back:
T1 = translation_matrix(-cx, -cy)
R  = rotation_matrix(np.deg2rad(theta))  
T2 = translation_matrix(cx, cy)

# Full translation matrix
M = T2 @ R @ T1

# Inversion mapping
# output pixel → where it came from in input
M_inv = np.linalg.inv(M)


# Apply transformation to image (manual warp)
output = np.zeros_like(img_arr)

for y_out in range(H):
    for x_out in range(W):
        # output pixel in homogeneous coords
        p_out = np.array([x_out, y_out, 1])

        # map back to input
        x_in, y_in, _ = M_inv @ p_out

        x_in = int(round(x_in))
        y_in = int(round(y_in))

        # bounds check
        if 0 <= x_in < W and 0 <= y_in < H:
            output[y_out, x_out] = img_arr[y_in, x_in]

# Display result
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img_arr)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title(f"Transformed (Rotated by {theta}°)")
plt.imshow(output)
plt.axis("off")

plt.show()

