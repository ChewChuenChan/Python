# create the user class and add following methods
# display_info(self) - 
#   Have this method print all of the users' details on separate lines.
# enroll(self) - 
#   Have this method change the user's member status to True 
#   and set their gold card points to 200.
# spend_points(self, amount) - 
#   have this method decrease the user's points by the amount specified.

# create a file with the User class
# including the __init__ with all the attributes, parameters and default values

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

# Add the enroll method to the User class
# Change the user's member status to True
# Set their gold card points to 200
# Bonus: Check if they are a member already,
# and if they are, print" User already a member", return False
# otherwider return True
    def enroll(self):
        if self.is_rewards_member== True:
            print(f"User already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

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



# In the outer scope, create a user instance
# call the display_info method to test
user1 =User("Alice", "Li","aliceli@gmail.com", "35", False, 0)
# user1.display_info()

#Implement enroll method and test by calling the method on the user in the outer scope
user1.enroll()
# user1.display_info()

# Implement the spend_points(self,amount) method
# Have the fisrt user spend 50 points
# call the display method on user1
user1.spend_points(50)
user1.display_info()


# Make 2 more instancesf of User class
# Instance1:
user2 = User("Simon", "Li","simonli@gmail.com", "40", True, 81)
# user2.display_info()

#Have the 2nd user enroll
user2.enroll()
# user2.display_info()

#have the 2nd user spend 80 points
# call the display method on user2
user2.spend_points(80)
user2.display_info()


# INstance2:
user3 = User("Daniel", "li","danielli@gmail.com","10",True,10)
# user3.display_info()

#prevent over-spending
# call the spend_points method with 40 points on 3rd user
# call the display method on user3
user3.spend_points(40)
user3.display_info()

