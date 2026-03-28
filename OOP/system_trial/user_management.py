from employee import Developer, Accountant

class UserManagement:
    def __init__(self):
        self.employees_db: list[dict] = []
        self.id = 1
    
    def main(self):
        while True:
            self.menu()
    
    def menu(self):    
        print("\nWhat do you want to do today?")
        print("1. Add employee")
        print("2. View all employees")
        print("3. Delete Employee")
        print("4. Exit program")
        
        choice = input("\nEnter choice (1/2/3/4): ")
        
        if choice == "1":
            print("\nCreating a new employee...")
            self.add_employee()
        elif choice == "2":
            print("\n===== All Employees =====")
            self.view_all_employees(self.employees_db)
        elif choice == "3":
            self.delete_employee()
        elif choice == "4":
            print("Exiting...")
            exit()
        else:
            print("Invalid input!")
            
    def add_employee(self):
        details: dict = self.get_employee_details()
        
        name = details["name"]
        number = details["number"]
        role = details["role"]
        id = details["id"]
        
        try:
            employee = self.create_employee(name, number, role, id)
            print(f"\nEmployee '{name}' created successfully!")
            
            self.employees_db.append(employee)
            
        except Exception as e:
            print(f"Error creating employee: {e}")
    
    def get_employee_details(self):
        try: 
            name = input("Enter a name: ")
            number = int(input("Enter a your number: "))
            role = input("Enter the role of the employee: ")
            id = self.id
            self.id += 1
        except Exception as e:
            print(f"Error fetchiing data: {e}")
            
        return {"name": name, "number": number, "role": role, "id": id}
        
    def create_employee(self, name, number, role, id):
        if role.lower() == "developer":
            employee = Developer(name, number, id)
        elif role.lower() == "accountant":
            employee = Accountant(name, number, id) 
            
        return employee 
    
    def delete_employee(self):
        self.view_all_employees(self.employees_db)
       
        print("\nWhich of them do you want to delete?")
        employee_to_delete = int(input("Enter employee ID: "))
        print("\nDeleting employee...")
       
        try:
            for employee in self.employees_db:
                if employee.id == employee_to_delete:
                    confirm = input(f"\sAre you sure you want to confirm employee: {employee.name}, ID: {employee.id} ? (yes/no): ")
                   
                    if confirm.lower() == "yes":
                       self.employees_db.remove(employee)
                       print(f"Employee '{employee.name}' deleted successfully!")
                    
                    else:
                        print("Aborting deletion...")
                        return self.main()
                
                else:
                    print("Employee not found!")  
        except Exception as e:
            print(f"Error deleting employee: {e}")

    def view_all_employees(self, employees):
        if len(employees) == 0:
                print("No employees found")
                return self.main()
            
        for employee in employees:
            employee_data = self.display_employee_details(employee)  
            print(employee_data) 
            
        
    def display_employee_details(self, employee: object) -> dict:
        return {"name": employee.name, "number": employee.number, "role": employee.role, "id": employee.id}

if __name__ == "__main__":
    management_system = UserManagement()
    management_system.main()