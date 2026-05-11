my_dict = {
    'name': 'Jay',
    'country': 'Nigeria',
    'age': 20,
    'level of education': 'University',
    'is tall': True,
    'hobbies': ['programming', 'reading', 'learning'],
}

name = my_dict['name']
if name == my_dict.get('name'):
    print("They are the same")
number_of_elements = len(my_dict)

print(my_dict)
print(f"The number of elements in the dictionary is: {number_of_elements}")
print(f"The name is: {name}")
print(f"Is {name} tall: ", my_dict['is tall'])
print(type(my_dict))
#print(my_dict.keys()[1], type(my_dict.keys()))

# .update() takes another dictionary as argument and adds its key-value pairs the dict or overwrite existing pairs
new_dict = {"is_smart": True}
my_dict.update(new_dict)
print(my_dict)