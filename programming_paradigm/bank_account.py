class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: {amount}. New balance: {self.account_balance}."
        else:
            return "Deposit amount must be positive."
        
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return f"Withdrew: {amount}. New balance: {self.account_balance}."
            else:
                return "Insufficient funds for this withdrawal."
        else:
            return "Withdrawal amount must be positive."
        
    def display_balance(self):
        return f"Current Balance: {self.account_balance}."

