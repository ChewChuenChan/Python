# Create a BankAccount class with the attributes interest rate and balance
# The BankAccount class should have a balance. 
# When a new BankAccount instance is created, if an amount is given, 
# the balance of the account should initially be set to that amount; 
# otherwise, the balance should start at $0.
# The account should also have an interest rate in decimal format.

class BankAccount:
    all_accounts=[]
    def __init__(self, int_rate=float, balance=float): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        

# Add a deposit method to the BankAccount class
# Increases the account balance by the given amount
    def deposit(self, amount=float):
        self.balance = self.balance + amount
        return self

# Add a withdraw method to the BankAccount class
# Decreases the account balance by the given amount if there are sufficient funds
# If there is not enough money, 
# Print a message "Insufficient funds: Charging a $5 fee"
# and deduct $5
    def withdraw(self, amount=float):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
            print("Charging a $5 fee","\n")
            self.balance -= 5
        return self

#Add a display_account_info method to the BankAccount class
# print to the console:eg."Balance:$100"
    def display_account_info(self):
        print(f"Balance: $ {round(self.balance,2)}","\n")
        return self

# Add a yeild_interest method to the BankAccount class
# Increases the account balance by 
# the current balance * the interest rate
# as long as the balance is positive
    def yield_interest(self):
        if BankAccount.positive(self.balance):
            self.balance += (self.balance * self.int_rate)
        else:
            print("Insufficient Funds,no interest","\n")
        return self

# static method
# Testing if the different of balance and amount is positive
    @staticmethod
    def can_withdraw(balance,amount):
        if(balance - amount) < 0:
            return False
        else:
            return True

# static method
# Testing if the balance is positive
    @staticmethod
    def positive(balance):
        if balance > -1:
            return True
        else:
            return False

    @classmethod
    def print_all_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()


# Create 2 accounts
account1 = BankAccount(0.01,100.66)
account2 = BankAccount(0.01,300.33)

# accout1, make 3 deposits; 1 withdrawal, yield interest, & display the acoount's info
# in one line of code(chaining)
account1.deposit(10).deposit(10).deposit(10).withdraw(80).yield_interest().display_account_info()

# accout2, make 2 deposits; 4 withdrawal, yield interest, & display the acoount's info
# in one line of code(chaining)
account2.deposit(10).deposit(10).withdraw(20).withdraw(20).withdraw(10).withdraw(20).yield_interest().display_account_info()

BankAccount.print_all_info()
