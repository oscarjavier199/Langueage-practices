#using default values in function definitions

def pets(name, animal='cat'):
    print(f"I have a {animal.title()}, called {name.title()}")
    
pets(name = "Odin")

