#basic if-else program, if an alien is certain color a message will print
#at the end of the program there is a simplified and better code.

alien_color = 'green'.lower()
if 'green' in alien_color:
    print("You just earned 5 points 😯")
elif 'yellow' in alien_color:
    print("You earned 10 points 😏")
elif 'red' in alien_color:
    print("OMG! you just earned 15 points 🙃")
    
alien_color = 'Yellow'.lower()
if 'green' in alien_color:
    print("You just earned 5 points 😯")
elif 'yellow' in alien_color:
    print("You earned 10 points 😏")
elif 'red' in alien_color:
    print("OMG! you just earned 15 points 🙃")
    
alien_color = 'red'.lower()
if 'green' in alien_color:
    print("You just earned 5 points 😯")
elif 'yellow' in alien_color:
    print("You earned 10 points 😏")
elif 'red' in alien_color:
    print("OMG! you just earned 15 points 🙃")


#same previous program but making simpler if statements
alien_color = 'Yellow'.lower()
if 'green' in alien_color:
    points = 5
elif 'yellow' in alien_color:
    points = 10
elif 'red' in alien_color:
    points = 15

print(f"You just earned {points} points 😯")