# 1) Define a class for bank accounts
class BankAccount:
    # 2) Constructor: initialize account details
    def __init__(self, account_holder: str, balance: float, account_type: str):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    # 3) Method to deposit money
    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    # 4) Method to withdraw money
    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance")

    # 5) Method to display account details
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, "
              f"Type: {self.account_type}, "
              f"Balance: {self.balance}")
        

# 6) Main section: only runs when executed directly
if __name__ == "__main__":
    # 7) Create two different bank accounts
    acc1 = BankAccount("Aisha", 1000.0, "Savings")
    acc2 = BankAccount("Rohan", 500.0, "Current")

    # 8) Display initial details
    print("--- Initial Account Details ---")
    acc1.display_balance()
    acc2.display_balance()

    # 9) Perform deposits
    print("\n--- Deposits ---")
    acc1.deposit(500)   # Aisha adds money
    acc2.deposit(200)   # Rohan adds money

    # 10) Perform withdrawals
    print("\n--- Withdrawals ---")
    acc1.withdraw(300)   # Aisha withdraws successfully
    acc2.withdraw(800)   # Rohan tries to withdraw more than balance

    # 11) Final details
    print("\n--- Final Account Details ---")
    acc1.display_balance()
    acc2.display_balance()
