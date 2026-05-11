# Functions
# Functions are reusable pieces of code that perform a specific task.
# They can take inputs (arguments) and return outputs (results).

from tkinter.font import names

def greet(name, age):
    print("Hello " + name + ". You are ", str(age) + " years old")
name = input("Enter your name: ")
age = input("Enter your age: ")  
greet(name, age)    

# If you don't know the number of arguments, you can use *args to accept a variable number of arguments.
def greeting(*Xnames):
    #one by one
    for x in Xnames:
        print("Hello", name)
    print("Hellos", *Xnames)
greeting(name)  