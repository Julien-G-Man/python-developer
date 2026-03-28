import random

numbers = []
allowed = [0, 1]

for i in range(1000):
    number = random.choice(allowed)
    numbers.append(number)
    
print(numbers) 