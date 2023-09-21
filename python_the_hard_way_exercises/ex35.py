from sys import exit #exists program without raising error if input is not as expected

#! function is created
def gold_room():
    print("This room is full of gold. How much do you take?") #print message
    print("options: 0 or 1... maybe more?")
    choice = input("> ") #takes input from user
    
    if "0" in choice or "1" in choice: #if input is 0 or 1:
        how_much = int(choice) # the input is stored in variable how_much and converted to an int
    else: #if user does't type a valid format int, the next line will be printed
        dead("Man, learn to type a number!") #function call
    if how_much < 50: #if user's input is < 50 the next line will be printed
        print("Nice, you're not greedy, you win!")
        exit(0) #exits program without errors
    else: #if user chooses a value >50 the next line is executed
        dead("You greedy bastards!")

#! function is declared
def bear_room():
    print("There is a bear here.") #prints message
    print("The bear has a bunch of honey.") #prints message
    print("The fat bear is in front of another door") #prints message
    print("How are you going to move the bear?") #prints message
    print("options: take honey - taunt bear - open door") #prints message
    bear_moved = False #creates variable = to False

    while True: #while statement
        choice = input("> ") # takes input from user
    
        if choice == "take honey": #if user chooses 'take hone'. the function dead() will be called and the message will be stored in the why parameter in dead()
            dead("The bear looks at you then slaps your face off!")
        elif choice == "taunt bear" and not bear_moved: #if user chooses "taunt bear", the statement not bear_moved is = True
            print("The bear has moved from the door.")
            print("You can go through it now.")
            print("option: 'open door' or 'taunt bear'")
            bear_moved = True #variable is changed from False to True
        elif choice == "taunt bear" and bear_moved: #if user chooses "taunt bear" again the variable bear_moved would be False and the function dead() will be executed
            dead("The bear gets pissed off and chews your leg off :)") #function is called and executed, message is stored as parameter
        elif choice == "open door" and bear_moved: #if user chooses "open door", the function gold_
            gold_room() #call to gold_room function
        else: #else statement if user input is a not-defined option
            print("I got no idea what that means :(") #prints message

#! function definition
def cthulhu_room():
    print("Here you see the great evil Cthulhu") #prints message
    print("He, it, whatever stares at you and you go insane!") #prints message
    print("Do you flee for your life or eat your head?") #prints message
    print("options: Flee or head") #prints message
    
    choice = input("> ") #takes input from user
    
    if "flee" in choice: #if statement, if user inputs 'flee' in previous choice = input, it will take him to start function
        start() #function call to start function
    elif "head" in choice: #if user chooses "head" the function dead() will be called, it will take the message as parameter
        dead("well that was nasty!")
    else: #if user inputs any other message, the cthulhu_room() will be called again until user chooses one of the previous options
        cthulhu_room()

#! function definition 
def dead(why): #function takes one parameter (why) which acts as placeholder for later given values.
    print(why, "good job!!!") # takes parameter and prints message
    print("you're De4ad :(") #prints message
    print("Play again any other time!") #prints message


#! function definition:
def start():
    print("You are in a dark room.") #prints message
    print("There is a door to your right and left.") #prints message
    print("which one do you take?") #prints message
    print("options: left or right") #prints message
    
    choice = input("> ") #takes input from user
    
    if choice == "left": #if user chooses left, it take him to the function bear_room()
        bear_room()
    elif choice == "right": #if user chooses right it will take him to the function cthulhu_room()
        cthulhu_room()
    else: #if user inputs something else beside left or right it will display message:
        dead("You stumble around the room until you starve")
        
start()#call of function
        