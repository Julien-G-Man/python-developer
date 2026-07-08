from employee import Employee

class StorageSystem:
    def __init__(self):
        self.employee_db: list[Employee] = []
        
    def save(self, employee):
        self.employee_db.append(employee)
    
    def delete(self, employee):
        self.employee_db.remove(employee)
        
    def update(self, employee, name, number):
        employee._name = name
        employee._number = number
    
