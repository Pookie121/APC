
class BankAccount:
    counter = 1001

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.account_number = BankAccount.counter
        BankAccount.counter += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful:", amount)
        else:
            print("Transfer failed! Insufficient balance or invalid amount.")


# Create two bank account objects
a1 = BankAccount("Sakshi")
a2 = BankAccount("Priya")

# Deposit money
a1.deposit(5000)
a2.deposit(3000)

# Withdraw money
a1.withdraw(1000)

# Transfer money from a1 to a2
a1.transfer(2000, a2)

# Display final balances
print("\nAccount 1 Details:")
a1.display_balance()

print("\nAccount 2 Details:")
a2.display_balance()
