# Pivota - Digital Payments Solution
# Not AI, it's all done by me :)
import re
import datetime
from datetime import datetime

class Payment:
    def __init__(self, name: str, password: int, account_number: int, balance: float, is_authenticated: bool):
        self.name = name
        self.password = password
        self.account_number = account_number
        self.balance = balance
        self.is_authenticated = is_authenticated
        
    def save_information(self, name, password, account_number, balance):
        user_info = {
            'name': name, 
            'password': password, 
            'account_number': account_number, 
            'balance': balance
            }
        print(f"User details: {user_info}")
        
        return '\nInformation saved!✅'          
    
    def checkBalance(self, name, balance):
        print("\n===== My Balance =====")
        print(f"Hi, {name}. Your balance is {balance} FCFA.")
        return main()
    
    def makePayment(self, password, balance):
        print("\n===== Make Payments =====")
        
        receiver_number = int(input("Enter recepient number: "))
        amountSent = float(input("Enter the amount you want to send in FCFA: "))
        pin = int(input("Enter your pin to confirm payment: "))
        
        if amountSent > balance:
            print(f"Insufficient balance. You only have {balance} FCFA.")
            print("Transaction Failed! ❌")
            main()
        
        if pin == password:
            newBalance = balance - amountSent
            print("\nTransacation successful!✅")
            print(f'\nYou made a payment of {amountSent} FCFA to {receiver_number}.')
            print(f"Former balance: {balance}")
            print(f"Remaining balance: {newBalance}")
            balance = newBalance
            amount_to_deposit = amount_to_withdraw = 0
            
            print(self.save_transaction_history(receiver_number, amountSent, balance, amount_to_deposit, amount_to_withdraw))
            
        else:
            print("Error! Wrong transaction PIN.❌")
    
    def deposit(self, password, balance, amount_to_deposit: int):
        print("\n==== MAKE A DEPOSIT ====")
        amount_to_deposit = int(input("How much do you want to deposit: "))
        pin = int(input("Enter your pin: "))
        if pin == password:
            balance += amount_to_deposit
            return f"\nYou just made a deposit of {amount_to_deposit} FCFA. \nYour new balance is {balance} FCFA."
        else:
            print("\nError! Wrong transaction PIN. ❌")
            return "Transaction cancelled!"    
        
    
    def withdraw(self, password, balance, amount_to_withdraw: int):
        print("\n==== WITHDRAW ====")
        amount_to_withdraw = int(input("How much do you want to withdraw: "))
        pin = int(input("Enter your pin: "))
        if amount_to_withdraw < balance:
            if pin == password:
                balance -= amount_to_withdraw
                return f"\nYou just made a withdrawal of {amount_to_withdraw} FCFA. \nYour new balance is {balance} FCFA."
            else:
                print("\nError! Wrong transaction PIN. ❌")
        else:
            print("\nInsufficient balance!")        
            return "Transaction cancelled!"    
        
   
    def save_transaction_history(self, receiver_number, amountSent, balance, amount_to_deposit, amount_to_withdraw):
        self.receiver_number = receiver_number
        self.amountSent = amountSent
        amount_to_deposit = amount_to_deposit
        amount_to_withdraw = amount_to_withdraw
        
        transaction = {
            'receiver_number': receiver_number,
            'amount_sent': amountSent,
            'new_balance': balance, 
            'time': datetime.now()
        }
        
        return self.view_transaction_history(transaction)
    
    def view_transaction_history(self, transaction):
        print("\n===== Transaction History =====")
        print("Here's a review of your most recent transaction...")
        print(transaction)
            
               
    def logout(self, is_authenticated):
        self.is_authenticated = False
        print(f'Goodbye {self.name}. You have been logged out.')
        print(f"Authenticated?: {is_authenticated}")
        return      
    
    
def create_user():
    name = name
    password = password
    users = []
    users = users.append('user')
    return 'user'
   
def main():
    print("\n|============================================|")
    print("|===========| PIVOTA MICROFINANCE |==========|")
    print("|============================================|")
    print("\nWelcome to Pivota. The most reliable online payments service across The Congo.")   
    

    print("\nCreate an account to access all our services")
    name = input("Enter your username: ").capitalize()
    pwd1 = input("Enter 4 digit password: ")
    pwd2 = input("Confirm password: ")
    
    #ensure the two passwords match and are 4 digits
    if pwd1 == pwd2 and (len(pwd1) == len(pwd2) == 4):
        # Check if user entered multiple names and only take the first name
        names_entered = re.findall(r"\b\w+\b", name)
        if len(names_entered) > 1:
            name = names_entered[0] # only use first name

        name = name.capitalize()
        password = int(pwd1)
        is_authenticated = True
     
        print("\nAccount created successfully!✅")
        print(f"Welcome, {name}. You are now signed in.")
    else:
        print("\nError! The two passwords do not match or are not exactly 4 digits.❌")  
        exit()       
            
    # create object user1 with default balance 5k  
    balance = 50000
    account_number = 8165113449
    user1 = Payment(name, password, account_number, balance, True)
        
    print(user1.save_information(name, password, account_number, balance))
    
    print("\nWhat do you want to do today?")
    print("1. Check Balance")
    print("2. Make payment")
    print("3. Logout") 
    print("4. Deposit")
    print("5. Withdraw")
    print("0. Exit program entirely")
    
    choice = input("\nEnter choice (1/2/3): ")
    
    if choice == "1":
        if is_authenticated == True:
            print(user1.checkBalance(name, balance))
        else:
            print("Access Denied. User not authenticated.❌") 
            exit()   
            
    elif choice == "2":
        print(user1.makePayment(password, balance))
    elif choice == "3":
        print(user1.logout(is_authenticated))
    elif choice == "4":
        amount_to_deposit = 0
        print(user1.deposit(password, balance, amount_to_deposit))
    elif choice == "5":
        amount_to_withdraw = 0
        print(user1.withdraw(password, balance, amount_to_withdraw))        
    elif choice == "0":
        print("Exiting...")
        return exit()   
    else:
        print("Invalid input!") 
        return 

if __name__ == "__main__":
    main()
