# List of players
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
# print(players[0])
# print(players[0]["name"])
# Update the constructor to accept a dictionary with a single player's information
# instead of individual arguments for the attributes
class Player:

    
    def __init__(self, data):
            self.name     = data["name"]
            self.age      = data["age"]
            self.position = data["position"]
            self.team     = data["team"]

# kevin=Player(players[0])
obj_list=[]

for x in players:
    obj_list.append(Player(x))

for row in obj_list:
    print(f"{row.name} {row.age} {row.position} {row.team}")

# print(obj_list)
# this_player=Player()
# print(kevin.name)