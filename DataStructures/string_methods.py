sentence = "The name is Jay"

print(sentence[-8:-2])

# built-in functions
length = len(sentence)
print(f"Number of characters in {sentence} is {length}")

words = sentence.split()
print(f"The words found in {sentence}: {words}")

print(sentence.split('name'))
print(f"Upper case: {sentence.upper()}")
print(f"Lower case: {sentence.lower()}")
print(f"Sentence case: {sentence.capitalize()}")

students = ["Julien", "Derick", "Derick", "Paul"]

print(students)
st = "Derick"

# Loop through and delete every occurence of "Derick"
while st in students:
    students.remove(st)
    
print(students)        