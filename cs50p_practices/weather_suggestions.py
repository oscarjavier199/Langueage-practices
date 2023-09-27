#program will welcome user to a trip agency and then ask for a destination, then it will randomly choose from
#our three statements using random.choice() and give user a weather notice.

import random

#function
def trip_welcome():
    
    #welcome user
    print("welcome to tripcademy!")
    
    # program will ask user for destination
    destination = input("where are you going today? \n")
    
    #random.choice() will print randomly one out of our three statements
    weather = random.choice([f"Looks like {destination} is going to be a little rainy today, take an umbrella!", 
    f"Take your sunglasses because it's gonna be sunny in {destination}", f"Better pack your bag :( winter is here, {destination} will be really cold!"])
    print(weather)

    
trip_welcome()