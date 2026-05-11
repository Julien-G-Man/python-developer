def insertion_sort(arr):
    for i in range(1, len(arr)):
        j  = i 
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1],arr[j] = arr[j], arr[j - 1]
            j -= 1

arr = [2, 6, 5, 1, 3, 4, 14, 7, 100, 9, 16, 10, 15]
print(f"Normal: {arr}")
print(f"Sort function: {sorted(arr)}")

insertion_sort(arr)
print(f"Insertion sort: {arr}")


