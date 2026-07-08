import sys
from employee import EMPLOYEE_TYPES
from storage import StorageSystem

db = StorageSystem()
employees = db.employee_db

 
class UserManagement:
    def __init__(self):
        self.EMPLOYEE_TYPES = EMPLOYEE_TYPES
        self.id = 1
    
    def main(self):
        while True:
            self.menu()
    
    def menu(self):    
        print("\nWhat do you want to do today?")
        print("1. Add employee")
        print("2. View all employees")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Exit program")
        
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == "1":
            print("\nCreating a new employee...")
            self.add_employee()
        elif choice == "2":
            print("\n===== All Employees =====")
            self.view_all_employees(employees)
        elif choice == "3":
            self.update_employee_data(employees)
        elif choice == "4":
            self.delete_employee()
        elif choice == "5":   
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid input!")
            
            
    def add_employee(self):
        details: dict = self.get_employee_details()
        
        name = details.get("name")
        number = details.get("number")
        role = details.get("role")
        id = details.get("id")
        
        try:
            employee = self.create_employee(name, number, role, id)
            print(f"\nEmployee '{name}' created successfully!")
            
            db.save(employee)
            
        except Exception as e:
            print(f"\nError creating employee: {e}")
    
    
    def get_employee_details(self):
        try: 
            name = input("Enter a name: ")
            number = int(input("Enter a your number: "))
            role = input("Enter the role of the employee: ")
            id = self.id
            self.id += 1
            
            return {"name": name, "number": number, "role": role, "id": id}
        
        except Exception as e:
            print(f"Error fetching data: {e}")
        
        
    def create_employee(self, name, number, role, id):
        cls = self.EMPLOYEE_TYPES.get(role.lower())  
        if not cls:
            raise ValueError("Invalid employee role")  
        return cls(name, number, id) 
    
    
    def delete_employee(self):
        self.view_all_employees(employees)
       
        while True:
            employee_id_input = input("\nWhich employee do you want to delete? (Enter ID): ")
            try:
                employee_to_delete = int(employee_id_input)
                break
            except ValueError:
                print("Invalid input. Employee ID must be an integer. Please try again.")
        
        print("\nDeleting employee...")
       
        try:
            for employee in employees:
                if employee.id == employee_to_delete:
                    found = True
                    confirm = input(f"\nAre you sure you want to confirm employee >> name: {employee.name}, ID: {employee.id} (yes/no): ")
                   
                    if confirm.lower() == "yes" or confirm.lower() == "y":
                       db.delete(employee)
                       print(f"Employee '{employee.name}' deleted successfully!")
                    else:
                        print("Aborting deletion...")
                        return
                
            if not found:
                print("Employee not found!")  
        except Exception as e:
            print(f"Error deleting employee: {e}")


    def view_all_employees(self, employees: list[object]):
        if len(employees) == 0:
            print("No employees found")
            return 
        
        for employee in employees:
            try:
                self.display_employee_details(employee)  
            except Exception as e:
                print(f"Error in [view all employees]: {e}")
        
        
    def display_employee_details(self, employee: object):
        print(f"Name: {employee.name} \nNumber: {employee.number} \nRole: {employee.get_role()} \nID: {employee.id} \n")


    def update_employee_data(self, employees: list[object]):
        print("======Existing employees ======")
        self.view_all_employees(employees)
        
        while True:
            employee_id_input = input("\nWhich employee do you want to edit? (Enter ID): ")
            try:
                employee_to_update = int(employee_id_input)
                break
            except ValueError:
                print("Invalid input. Employee ID must be an integer. Please try again.")
        
        try:
            for employee in employees:
                if employee_to_update == employee.id:
                    name = input("Enter new name: ")
                    number = input("Enter new number: ")
                    db.update(employee, name, number)
                    print(f"\nEmployee edited successfully!")
                    return
            print("Employee not found!")
        except Exception as e:
            print(f"\nError editing employee: {e}")

if __name__ == "__main__":
    management_system = UserManagement()
    management_system.main()