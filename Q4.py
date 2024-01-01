#WAP to create a class representing a bank. Include methods for managing customer accounts and transactions.
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = {'balance': initial_balance}
            print(f"Account {account_number} created with an initial balance of Rs{initial_balance}.")
        else:
            print(f"Account {account_number} already exists.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited ${amount} into account {account_number}. New balance: Rs{self.accounts[account_number]['balance']}.")
        else:
            print(f"Account {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]['balance']:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew ${amount} from account {account_number}. New balance: Rs{self.accounts[account_number]['balance']}.")
            else:
                print(f"Insufficient funds in account {account_number}.")
        else:
            print(f"Account {account_number} does not exist.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        else:
            print(f"Account {account_number} does not exist.")
            return None

bank = Bank()

bank.create_account("123456", 1000)
bank.create_account("789012", 500)

bank.deposit("123456", 200)
bank.withdraw("789012", 100)
bank.withdraw("123456", 1500) 
print("Account 123456 Balance:", bank.check_balance("123456"))
print("Account 789012 Balance:", bank.check_balance("789012"))
print("Account 999999 Balance:", bank.check_balance("999999"))  