"""
Insertion sort builds a sorted list by inserting each new item into its right
position in the already sorted part.

It is fast on small or nearly sorted data, but has O(n²) worst-case time.
"""


def insertion_sort(numbers: list):
    for i in range(1, len(numbers)):
        number_to_order = numbers[i]
        j = i - 1
        while j >= 0 and number_to_order < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = number_to_order
    return numbers

numbers = [5, 4 ,7, 2, 1, 0, 3, 5, 7, 24, 76 ,13 , 46, 83, 37, 79, 6, 90]
print(insertion_sort(numbers))