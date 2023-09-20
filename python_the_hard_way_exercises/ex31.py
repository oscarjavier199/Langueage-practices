#prints message
print("""you enter a dark room with two doors. 
Do you go through door # 1, door #2 or door 3?""")

#takes input from user
door = input("> ")

#main if statement - user chooses door 1:
if door == "1":
    print("There's a giant bear here, he's hungry...")
    print("What do you do?")
    print("1. take the cake.")
    print("2. scream at the bear.")
    print("3. R.U.N for your life")

#takes input from user and stores it in bear variable
    bear = input("> ")

#if statement inside if statement -  user inputs 1:
    if bear == "1":
        print("The bear eats your face off. Good job!")

#if user inputs 2
    elif bear == "2":
        print("The bear eats your legs off, Good Job!")

#if user inputs 3:
    elif bear == "3":
        print("""What were you thinking?
a bear is way faster than a human!""")

#if user inputs any other input:
    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away")

#door #2
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    print("4. I have no idea what the heck is going on in here!")

#we store the answer or input in the variable insanity
    insanity = input("> ")
    
#if user inputs option 1 or option 2
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job")

#if user inputs option 3
    elif insanity == "3":
        print("""wait... what? 
just give me a gun already""")

#if user inputs option 4
    elif insanity == "4":
        print("""I just wanted to go home...
But now you're gone.. if you get what that means, it means you're de4d""")

#if user inputs any other input
    else:
        print("the insanity rots your eyes into a pool of muck.")
        print("Good job!")

#is user chooses door 3:
elif door == "3":
    print("""Congrats!
now Pinhead and Freddy Krueger will hunt you..
sleep or awake, won't matter...
say your last words or pray if you want.""")

#wrapping up main if statement:
else:
    print("You stumble around and fall on a knife and die. Good job!")