class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    
    def add_item(self, item_name):
        valid_items = ["cacao tree",  "kotatsu", "rattan armchair", "acoustic guitar", "ironwood kitchenette"]
        
        if item_name in valid_items:
            self.furniture.append(item_name)
            
    
            
def of_personality_type(townies, personality_type):
    
    res = []
    for v in townies:
        if v.personality == personality_type:
            res.append(v.name)
    
    return res   

def message_received(start_villager, target_villager):
        
        current = start_villager
        
        while current != None:
            if current.neighbor == target_villager:
                return True
            else:
                current = current.neighbor
        return False    
'''
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)
'''
'''
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
'''

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))