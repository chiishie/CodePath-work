def total_treasures(treasure_map):
    
    sum = 0
    for key, values in treasure_map.items():
        sum = sum + values
    
    return sum

def can_trust_message(message):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    lowercase_set = sorted(set(lowercase_letters))
    message_set = set(message.replace(" ", ""))
    
    sorted_message = sorted(message_set)
    
    if sorted_message == lowercase_set:
        return True
    
    return False
            
def analyze_library(library_catalog, actual_distribution):
    
    res = {}
    
    for key, val in library_catalog.items():
        res[key] = actual_distribution[key] - library_catalog[key]
        
    return res
        
def find_common_artifacts(artifacts1, artifacts2):
    
    a1 = set(artifacts1)
    
    res = []
    
    for item in artifacts2:
        if item in a1:
            res.append(item)
            
    return res

def declutter(souvenirs, threshold):
    
    map = {}
    res = []
    
    for item in souvenirs:
        if item not in map:
            map[item] = 1
        else:
            map[item]+=1
    
    for item in souvenirs:
        if map[item] < threshold:
            res.append(item)

    return res        

def num_of_time_portals(portals, destination):
    
    count = 0
    map = {}
    j = 1
    
    for i in range(len(portals)):
        for j in range(len(portals)):
            if i != j:
                if portals[i] + portals[j] == destination:
                    count+=1
                    
    return count       

def find_treasure_indices(gold_amounts, target):
    
    left = 0
    right = len(gold_amounts) - 1
    map = {}
    
    for i, value in enumerate(gold_amounts):
        complement = target - value
        if complement in map:
            return [map[complement], i]
        else:
            map[value] = i
    
    return []

def find_attractions(tourist_list1, tourist_list2):
    
    map = {}
    res = []
    
    for i, item in enumerate(tourist_list1):
        if item in tourist_list2:
            map[item] = i + tourist_list2.index(item)
        
    return [key for key, value in map.items() if value == min(map.values())]



message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"
message3 = "a quick brown fox jumps over the lazy dog and vexes a wizard while flying kites near a gym in hawaii amid quaint zebras playing jazz"

print(can_trust_message(message1))
print(can_trust_message(message2))
print(can_trust_message(message3))


treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map","map", "statue"]
threshold1 = 3

print(declutter(souvenirs1, threshold1))

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold2 = 2

print(declutter(souvenirs2, threshold2))

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Colosseum","Trevi Fountain","Pantheon","Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Disneyland","Eiffel Tower","Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach","mountain","forest"]
tourist_list2 = ["mountain","beach","forest"]

print(find_attractions(tourist_list1, tourist_list2))