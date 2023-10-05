# passing multiple parameters to a function definiton and giving multiple arguments
# in a function 

#! possitional arguments

def pets(pet, pet_name):
    print(f"\n\tI have a {pet.title()}, called {pet_name.title()}\n")
    
pets('cat', 'odin')
pets('snake', 'snape')