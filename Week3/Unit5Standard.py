class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) > 20 or any(not (char.isalpha() or char == " ") for char in new_catchphrase):
            print("Invalid catchphrase")
        else:
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")

        
apollo = Villager('Apollo', "Eagle", "pah")
bones = Villager('Bones', "Dog", "yip yip")
    
print(bones.greet_player("Tram"))

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)