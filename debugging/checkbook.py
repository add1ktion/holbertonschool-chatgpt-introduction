#!/usr/bin/python3
"""
Python Checkbook - Error Handling Implementation
Interactive banking application with robust input validation.
Prevents crashes from invalid numeric input.
"""

class Checkbook:
    """
    Simple checkbook class for managing bank account balance.
    
    Attributes:
        balance (float): Current account balance (default 0.0)
    """
    
    def __init__(self):
        """
        Initialize Checkbook with zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit positive amount to account balance.
        
        Args:
            amount (float): Amount to deposit (> 0)
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw amount if sufficient funds available.
        
        Args:
            amount (float): Amount to withdraw (> 0)
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display current account balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main program loop with comprehensive error handling.
    Handles ValueError from float() conversion and invalid actions.
    """
    cb = Checkbook()
    
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            print("Thank you for using Checkbook!")
            break
        elif action == 'deposit':
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    cb.deposit(amount)
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number (e.g., 100.50).")
        elif action == 'withdraw':
            while True:
                try:
                    amount = float("Enter the amount to withdraw: $"))
                    cb.withdraw(amount)
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number (e.g., 50.25).")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Use: deposit, withdraw, balance, exit")

if __name__ == "__main__":
    """
    Program entry point.
    """
    main()
