# https://pypi.org/project/banking-system/
import banking_system as bs
from banking.account import Account

account = Account("Jay Prince", 1500.0)
print(account)

#making a  deposit
from banking_system.account import Account
account.deposit(500.0)
print(account.balance)

# Making a withdrawal
from banking_system.account import Account
account = Account("Jay Prince", 1500.0)
account.withdraw(200.0)
print(account.balance)

# Performing a transaction
from banking_system.account import Transacction
sender =  Account("1123456", 1000.0)
receiver = Account("654321", 600.0)
trnsaction = Transaction(sender, receiver, 500.)

# process the transaction
transaction.process()
print(transaction)