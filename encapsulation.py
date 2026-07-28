# Program to demonstrate Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def show_balance(self):
        print("Current Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited:", amount)

# Creating an object
account = BankAccount(5000)

account.deposit(1000)
account.show_balance()