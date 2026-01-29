"""
Destructors are special functions that are called when an object gets deleted. 
In Python, the __del__() method is commonly used as the destructor and is called when an object is deleted.
"""

class ClassSchedule:
    def __init__(self, course):
        self.course = course
        
    def __del__(self):
        print(f"{self.course} has been deleted")
        
        
sched = ClassSchedule("Math")
print(f"{sched.course} has been created")
del sched