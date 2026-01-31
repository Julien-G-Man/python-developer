from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = Image.open("images/.jpg")

# Convert to NumPy array
img_array = np.array(img)
print("Image shape: ", img_array.shape)
print("\nData type: ", img_array.dtype)

"""
- Shape tells you grayscale vs RGB
- dtype tells you how arithmetic behaves
"""

# Invert using pure patrix math
inverted_img = 225 - img_array
print("\nInverted image: \n", inverted_img)

inverted_pil = Image.fromarray(inverted_img)
inverted_pil.save("images/quote.jpg")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img_array)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Colour Inverted")
plt.imshow(inverted_img)
plt.axis("off")

plt.show()


