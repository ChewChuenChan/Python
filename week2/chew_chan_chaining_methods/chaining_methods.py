#Update previous assignment so that each instance's methods are chained.

import email
from xmlrpc.client import boolean


class User:
    pass
    def __init__(self,first_name="",last_name="",email="",age=int,is_rewards_member=bool,gold_card_points=int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member= is_rewards_member
        self.gold_card_points= gold_card_points
        

# Add the display_info(self)method to the User class
# Print all the users' details on separate lines
    def display_info(self):
        print(f"My first name is {self.first_name}.")
        print(f"My last name is {self.last_name}.")
        print(f"My email is {self.email}.")
        print(f"I am {self.age} year old.")
        print(f"I am reward member. It is {self.is_rewards_member}")
        print(f"I have {self.gold_card_points} gold card points.")
        return (self)

# Add the enroll method to the User class
# Change the user's member status to True
# Set their gold card points to 200
# Add return self for chaining
    def enroll(self):
        if self.is_rewards_member== True:
            print(f"User already a member")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
        
# Add the spend_points method to the User class
# Decrease the user's points by the amount of specified.
# Bonus: Make sure they have enough points to sepnd that amount and handle appropriately
    def spend_points(self,amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
            if self.gold_card_points > 1:
                pass
            else:
                print(f"You have 1 point left. It's time to enroll more points")
        else:
            print(f"Dear {self.first_name}, You only have {self.gold_card_points} gold coins left")
            print(f"Not enough points,please enroll more points")
        return self


# In the outer scope, create 3 user instances
user1 =User("Alice", "Li","aliceli@gmail.com", "35", False, 0)
user2 = User("Simon", "Li","simonli@gmail.com", "40", True, 81)
user3 = User("Daniel", "li","danielli@gmail.com","10",True,10)

#Implement chanining method to call functions
user1.display_info().enroll().spend_points(50).display_info()
user2.display_info().enroll().spend_points(80).display_info()
user3.display_info().enroll().spend_points(50).display_info()
