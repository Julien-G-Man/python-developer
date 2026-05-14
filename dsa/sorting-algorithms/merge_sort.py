"""
Merge sort is a divide-and-conquer sorting algorithm that splits a list into
smaller parts, sorts them, and then merges them back together.

It runs in O(n log n) time and uses extra space, so it is a good choice for
larger datasets when consistent performance matters.
"""


def merge_sort(numbers: list):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left_half = numbers[:mid]        
        right_half = numbers[mid:] 
        merge_sort(left_half)       
        merge_sort(right_half)  
        
        # indexes of new left side, right side and merged
        i = j = k = 0     
        while i < len(left_half) and j <  len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else: 
                numbers[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1
    return numbers
            
            
numbers = [5, 4 ,7, 2, 1, 0, 3, 5, 7, 24, 76 ,13 , 46, 83, 37, 79, 6, 90]
print(merge_sort(numbers))