"""
Quick sort is a divide-and-conquer, in-place sorting algorithm that picks a
pivot, partitions the list around the pivot, and recursively sorts the parts.

Average Time: O(n log n), Worst: O(n²) (rare with good pivot choice)
Space: O(log n) expected for recursion

Use quick sort for large datasets when average-case speed and low extra
memory are desired; prefer randomized or median-of-three pivot selection to
avoid worst-case behavior.
"""

def quicksort(numbers: list, first_index: int, last_index: int):
    if first_index < last_index:
        partition_index = partition(numbers, first_index, last_index)
        quicksort(numbers, first_index, partition_index - 1)
        quicksort(numbers, partition_index + 1, last_index)
    return numbers


def partition(numbers, first_index, last_index):
    pivot = numbers[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index
    while True:
        while numbers[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1
        while numbers[right_pointer] > pivot and right_pointer >= first_index:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        numbers[left_pointer], numbers[right_pointer] = numbers[right_pointer], numbers[left_pointer]
    numbers[first_index], numbers[right_pointer] = numbers[right_pointer], numbers[first_index]
    return right_pointer


numbers = [5, 4 ,7, 2, 1, 0, 3, 5, 7, 24, 76 ,13 , 46, 83, 37, 79, 6, 90]
print(quicksort(numbers, first_index=0, last_index=len(numbers) - 1))