class Employee:
    """ Blueprint class for all employees """
    name: str
    number: int
    role: str
    id: int
    is_admin: bool
    
    def __init__(self, name, number, id):
        self.name = name
        self.number = number
        self.role = self.get_employee_role()
        self.id = id
        
    def work(self, name):
        print(f"{name} is working")
        
    def get_employee_role(self):
        return self.role
        

# inheritance
class Developer(Employee):
    """Blueprint class for all developers, inherits from Employee"""
    def __init__(self, name, number, id):
        self.role = self.get_employee_role() #abstraction
        super().__init__(name, number, id)
        
    # polymorphism
    def work(self):
        """Same method, different Employees, different functionality"""
        print(f"{self.name} is coding")
        
    def get_employee_role(self):
        return "Developer"


class Accountant(Employee):
    """Blueprint class for all accountants, inherits from Employee"""
    def __init__(self, name, number, id):
        self.role = self.get_employee_role()
        super().__init__(name, number, id)
        
    # polymorphism
    def work(self):
        """Same method, different Employees, different functionality"""
        print(f"{self.name} is counting money")
        
    def get_employee_role(self):
        return "Accountant"
        
        
# instantiation of a class
mark = Developer("Mark", 1000, 1)
mark.work()
        