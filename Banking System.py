'''
Python OOP Mini-Project
'''
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to Alex Banking System")
  
    def deposit(self):
        amount=float(input
                     ("Enter amount you would like to be deposit in USD: "))
        self.balance += amount
        print(f"${amount} Deposited")
  
    def withdraw(self):
        amount = float(input
                       ("Enter amount you would like to be withdraw in USD "))
        if self.balance>=amount:
            self.balance-=amount
            print(f"${amount} Withdrawn")
        else:
            print("\n Insufficient balance  ")
  
    def display(self):
        print(f"${self.balance} left")
  
# Driver code
   
# creating an object of class
Alex = Bank_Account()
   
# Calling functions with that class object
Alex.deposit()
Alex.withdraw()
Alex.display()