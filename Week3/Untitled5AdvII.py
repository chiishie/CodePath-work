class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
        
    def add_item(self, item_name):
        self.items.append(item_name)

def print_results(race_results):
    for player in race_results:
        print("1. " + player.character)

def get_place(my_player):
    count = 1
    while my_player.ahead != None:
        my_player = my_player.ahead
        count += 1
    
    return count
        
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
player2_rank = get_place(peach)
player3_rank = get_place(mario)

print(player1_rank)
print(player2_rank)
print(player3_rank)

player_one = Player("Yoshi", "Super Blooper", None)
print(player_one.character)
print(player_one.kart) 
print(player_one.items)    

player_one = Player("Yoshi", "Dolphin Dasher", None)
print(player_one.items)

player_one.add_item("red shell")
print(player_one.items)

player_one.add_item("super star")
print(player_one.items)

player_one.add_item("super smash")
print(player_one.items)

peach = Player("Peach", "Daytripper", None)
mario = Player("Mario", "Standard Kart M", None)
luigi = Player("Luigi", "Super Blooper", None)
race_one = [peach, mario, luigi]

print_results(race_one)