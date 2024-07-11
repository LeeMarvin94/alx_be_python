#!/usr/bin/python3
#python script that contains a class for bank related operations

class BankAccount:

    # construction definition
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    #method's definition
    def deposit(self, amount):
        self.account_balance += amount
    #method's definition
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    #method's definition
    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}.00')

