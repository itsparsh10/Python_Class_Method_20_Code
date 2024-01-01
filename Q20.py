# Build a simulation of an ATM system with classes for accounts, transactions, and
# users. Implement methods for withdrawing cash, checking balances, and handling
# PIN verification.
class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

class Transaction:
    @staticmethod
    def verify_pin(account, entered_pin):
        return account.pin == entered_pin

class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account

account1 = Account(account_number="123456789", pin="1234", balance=10000)

user1 = User(name="Sparsh", account=account1)

entered_pin = input("Enter your PIN: ")
if Transaction.verify_pin(account1, entered_pin):
    print(f"Hello, {user1.name}!")
    print(f"Your current balance is: Rs{user1.account.check_balance()}")

    withdrawal_amount = float(input("Enter the withdrawal amount: "))
    print(user1.account.withdraw_cash(withdrawal_amount))
else:
    print("Invalid PIN. Transaction failed.")
