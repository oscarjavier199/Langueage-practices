from sys import exit

def door_4():
    pass

def door_3():
    pass

def door_2():
    pass

def door_1():
    print("-" * 15)
    print("You hear people screaming")
    print(" begin for help or relief...")
    print("then you hear a malevolent laugh and you see his shadow behind red smoke")
    print("freddy kruger is in front of you...")
    print("what do you do?")
    print("options: punch him - run - go back and close the door")
    user_choice = input("> ")
    if user_choice == "punch him":
        print("-" * 15)
        print("Did you really try to punch a dude with blades in his hands?")
        print("...\n")
        print("Your dead obviously")
        print("-" * 15)
        print("do you want to try again?")
        print("yes or no: ")
        second_choice = input("> ")
        if second_choice == "yes":
            game_start()
        elif second_choice == "no":
            print("See ya looser!")
        else:
            print("See you tonight...")
    elif user_choice == "run":
        print("who can possibly be faster than you?")
        print("...")
        print("I'll give you a clue")
        print("FREDDY KRUGER")
        print("You're gone man, goodbye")
        print("-" * 15)
        print("GAME OVER")
    elif user_choice == "go back" or "close the door" or "go back and close the door":
        print("good choice... ")
        print("It was all a dream")
        print("Goodbye")
        

def game_start():
    print("we have such sight to show you...")
    print("-" * 15)
    print("Your are trapped in a room with four dors")
    print("Red door, Black door, Withe door and brown door")
    print("-" * 15)
    print("which one do you choose?")
    user_choice = input("> ")
    if user_choice == "red door":
        door_1()
    elif user_choice == "black door":
        door_2()
    elif user_choice == "white door":
        door_3()
    elif user_choice == "brown door":
        door_4()
        
game_start()
    



