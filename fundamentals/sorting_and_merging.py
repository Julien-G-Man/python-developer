nums = [44,57,2,1,45,6,7,49,2,32]

print(f"Original: {nums}")
print(f"Sorted: {sorted(nums)}")

unique = list(set(nums))
print(f"Unique: {unique}")

sorted_unique = sorted(unique)
print(f"Sorted unique: {sorted_unique}")

dict1 = {"a": 1, "b": 3, "c": 5}
dict2 = {"c": 5, "d": 6}
merged = dict1 | dict2
print(merged)

# list comprehension
squares = [x**2 for x in range(5)]
print(squares)
