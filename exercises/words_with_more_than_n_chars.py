"""
You are given a list of words. Your task is to count 
how many words have more than n characters.
1. Loop through the list and check the length of each word.
2. Count words with more than n characters.
"""

words = ['apple', 'banana', 'grape', 'watermelon', 'fig', 'pineapple', 'blackberry']
n = 5

list = []
for i in words:
    if len(i) > n:
        list.append(i)
print(list)   
print(f"No. of words with more than {n} characters: {len(list)}")        
     


# otherwise
count = 0
for word in words:
    if len(word) > n:
        count += 1
print(f"No. of words with more than {n} characters: {count}")        