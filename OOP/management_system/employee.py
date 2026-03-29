class Employee:
    """ Blueprint class for all employees """
    def __init__(self, name, number, id):
        self._name = name
        self._number = number
        self._id = id
        
    @property
    def id(self):
        return self._id
        

# inheritance
class Developer(Employee):
    """Blueprint class for all developers, inherits from Employee"""
        
    # polymorphism
    def work(self):
        """Same method, different Employees, different functionality"""
        print(f"{self._name} is coding")
        
    def get_role(self):
        return "Developer"


class Accountant(Employee):
    """Blueprint class for all accountants, inherits from Employee"""
    
    # polymorphism
    def work(self):
        """Same method, different Employees, different functionality"""
        print(f"{self._name} is counting money...")
        
    def get_role(self):
        return "Accountant"
        

class Teller(Employee):
    def work(self):
        print(f"{self._name} is delivering money...")
        
    def get_role(self):
        return "Teller"
 

class Manager(Employee):
    def work(self):
        print(f"{self._name} is managing bank officers...")
        
    def get_role(self):
        return "Manager" 


EMPLOYEE_TYPES = {
    "manager": Manager,
    "developer": Developer,
    "accountant": Accountant,
    "teller": Teller
} 
    
        