"""
Bubble sort swaps adjacent items until the list is ordered.

It is simple, stable, and in-place, but slow on large inputs. Best for
teaching or very small lists.
"""

def bubble_sort(numbers: list):
    length = len(numbers)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]  
    return numbers


def bubble_sort_2(numbers: list):
    length = len(numbers)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(length - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                is_sorted = False
        length -= 1
    return numbers

numbers = [5, 4 ,7, 2, 1, 0, 3, 5, 7, 24, 76 ,13 , 46, 83, 37, 79, 6, 90]
print(bubble_sort(numbers))
print(bubble_sort_2(numbers))



"""
Use bubble sort mainly for teaching or tiny datasets.
For production code, faster algorithms are usually better.
"""
