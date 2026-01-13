"""
Matplotlib helps you creae=te charts and plots.
"""

import matplotlib.pyplot as plt
fruits = ['Apples', 'Bananas', 'Cherries']
sales = [20, 14, 31]
plt.bar(fruits, sales) #plt.plot(x, y)
plt.title("Fruit Sales Plot")
plt.show()