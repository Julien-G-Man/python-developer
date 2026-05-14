"""
Selection sort repeatedly picks the smallest item from the unsorted part and
puts it in the next position.

It runs in O(n²) time, uses O(1) space, and is mostly useful for tiny lists or
teaching in-place sorting.
"""

# python cheat I just made :)
# I'm not even sure it's sorting lol :()
# O(n) time complexity
def selection_sort_cheat(numbers: list):
    new_numbers = []
    for i in  range(len(numbers) - 1):
        new_numbers.append(min(numbers))
        numbers.remove(min(numbers))
    return new_numbers


def selection_sort(numbers: list):
    length = len(numbers)
    for i in range(length - 1):
        lowest = numbers[i]
        index = i
        for j in range(i + 1, length):
            if numbers[j] < lowest:
                index = j
                lowest = numbers[j]
        numbers[i], numbers[index], numbers[index], numbers[i]
    return numbers
    

numbers = [5, 4 ,7, 2, 1, 0, 3, 5, 7, 24, 76 ,13 , 46, 83, 37, 79, 6, 90]
print(selection_sort_cheat(numbers))