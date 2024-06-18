# 1. Account balance exercise - classes and methods

"""
To access this class from console:
from Acc_Balance import Account
define instance, for eg a = Account("Sam", 100)
and run it as a.deposit or a.withdrawal
"""

class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, dept_amt):
        self.balance = self.balance + dept_amt #can be replaced with +=dept.amt
        print(f"Deposited {dept_amt} to the balance")
    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt #can be replaced with -=wd.amt
            print(f"Withdrawal {wd_amt} accepted!")
        else:
            print("Sorry, not enough funds available.")
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"