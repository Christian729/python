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
# this returns kevin durant
# print(kevin["name"])

#challenge 1
class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]

    def show_stats(self):
        print(f"\n Name: {self.name} \n Age: {self.age} \n Position: {self.position} \n Team: {self.team}")
        return self

#challenge 2
# kevin = Player(kevin)
# jason = Player(jason)
# kyrie = Player(kyrie)

# kyrie.show_stats()

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


# challenge 3 time

# so let's understand lists n dictionaries 

#players is a list
List = ['a', 'b', 'c', 'd']
# print(List[2])


# 1. this makes kevin an object
kevin = Player(players[0])
# print(kevin["age"])


# these lines print kevin's entire dictionary 
# player = players[0]
# print(player)


# players_name = players[0]["name"]
# print(players_name)

# the code above and below do the same thing

# 2. this prints kevin's name
#print(players[0]["name"])

new_team = []
for player_dict in players:
    player= Player(player_dict)
    new_team.append(player)
    player.show_stats()

#print(new_team)
