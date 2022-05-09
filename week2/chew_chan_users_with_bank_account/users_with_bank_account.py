# Update your existing User class to have an association with the BankAccount class. 

from urllib.parse import non_hierarchical


class BankAccount:
    account_type= ""
    all_accounts=[]
    def __init__(self, int_rate=float, balance=float(0)): 
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


class User:
    def __init__(self,name=None,email=None, BankAccount=None):
        self.name = name
        self.email = email
        self.account = BankAccount
        
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User = {self.name}  {self.account.account_type} = ${round(self.account.balance,2)}")
        return self

    def transfer_money(self,amount,other_user):
        self.account.balance = self.account.balance - amount
        other_user.account.balance = other_user.account.balance + amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

Checking=BankAccount(0.02,100.55)
Saving=BankAccount(0.05,500.45)
alice_checking=User("Alice","aliceccc@gmail.com",Checking)
alice_saving=User("Alice","aliceccc@gmail.com",Saving)
alice_checking.account.account_type = "Checking"
alice_saving.account.account_type = "Saving"
alice_checking.make_deposit(10.66).display_user_balance()
alice_saving.make_withdrawal(10.11).display_user_balance()
alice_checking.transfer_money(20,alice_saving)