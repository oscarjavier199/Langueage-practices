#program to practice boolean operators with simple if statements

#program will test only if statements, not elif, not else, only if
people = 30
cats = 70
dogs = 5
birds = 100
bird_hunters = 100

if people < cats:
    print("Too many cats! The world is doomed!") #will print this one
if people > cats:
    print("Not many cats! the world is sad :(")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry") #will print this one
    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.") #will print this one
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("people are dogs")    
    
if cats > dogs:
    print("Cats win this one! sorry dogs")
if birds > cats:
    print("Goodbye cats, you'll be missed")
if birds == bird_hunters:
    print("see ya Birds")

birds = birds + 100

if birds > bird_hunters:
    print("birds win for now, coma back later hunters!")