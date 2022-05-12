# Set up a new file and add the Player class with the given constructor

# Challenge1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's
# information instead of individual arguments for the attributes

class Player:
    def __init__(self,data):
        self.name =data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    def print_player_info(self):
        print(f"Player name:{self.name}   age:{self.age}   position:{self.position}   team:{self.team}")

# Ninja Bonus: Add an @classmethod get_team(cls,team_list)that,
# given a list of dictionaries populates and returns a new list of Player objects
    @classmethod
    def get_team(cls,team_list):
        new_team_list =[]
        for dict in team_list:
            new_team_list.append(cls(dict))
        return new_team_list



# Challenge 2:Create instances using individial player disctionaries
# Create 3 instances of the Player class using the given dictionaries
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Create Player instances
player_kevin =Player(kevin)
player_jason =Player(jason)
player_kyrie =Player(kyrie)
player_kevin.print_player_info()
player_jason.print_player_info()
player_kyrie.print_player_info()



# Challenge3: Make a list of Player instances from a list of dictionaries
# given the example "list" of 'players'
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

#  write a for loop that will populate an empty list with "Player" object
new_team =[] 

# populate an empty list with "Player" object
for curr_player in players:
    new_team.append(Player(curr_player))

# print the output
for new_player in new_team:
    new_player.print_player_info()




# Ninja Bonus: print output
# Create new list from "Player" object
another_team=Player.get_team(players)    

# Print the list: for every "row" (instance) in the list "another_team", print row.name,row.age,row.postion and row.team out
for row in another_team:
    print(f"{row.name} {row.age} {row.position} {row.team}")
# Another way to print the list
for another_team_player in another_team:
    another_team_player.print_player_info() 