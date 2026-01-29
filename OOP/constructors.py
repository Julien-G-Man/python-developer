"""
Constructors are special functions that are executed when an object is instantiated. 
In Python, the __init__() function is used as the constructor and is called when creating an object.
"""

class Dog:
    def __init__(self, name):
        self.name = name
        
dog =  Dog("Max")
print(dog.name)