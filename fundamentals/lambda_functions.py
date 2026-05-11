"""
Lambda functions, also known as anonymous functions, are small, inline functions that can have any number of arguments but only one expression. 
They are defined using the lambda keyword and are typically used for short, simple operations.
"""

# Regular function 
def square(x):
    return x ** 2 

# Lambda function

square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))

# Basic syntax
# function = lambda [argument]: [expression]

add = lambda a, b: a + b
print(add(2, 3))


# Using Lambda functions with map()
"The map() function applies the given lambda function to each item in a list: "
numbers = [i for i in range(1, 6)]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
print([i**2 for i in range(1, 6)])


# Using Lambda with filter()
"The filter() function creates a new list of elements for which the given lambda function returns True: "
numbers = [i for i in range(1, 11)]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)
print([i for i in range(1, 11) if i % 2 == 0])


# Using Lambda with sorted()
"he sorted() function can use a lambda function as a key for custom sorting: "
students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 
sorted_students = sorted(students, key =lambda x: x[2])
print(sorted_students)