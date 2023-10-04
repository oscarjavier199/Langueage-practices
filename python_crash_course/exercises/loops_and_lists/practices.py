#rental car
'''
car = input("What kind of rental car are you looking for? >>> ")
print(f"Let me see if I can find you a {car.title()}")
'''

#restaurant sitting
'''
people = int(input("How many people are in your dinner group? >>> "))
if people > 8:
    print("Sorry you'll have to wait for a table")
else:
    print("Sure! please follow me")
'''

#multiples of ten
'''
number = input("Please enter a number, I'll tell you if it's multiple of 10 >>> ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple of ten 😊")
else:
    print(f"{number} is not multiple of 10 😒")
'''

#1 to 11
'''
number = 1
while number < 11:
    print(number)
    number += 1
'''

#parrot program

prompt = ("\nTell me something and I'll repeat it back to you ")
prompt += ("\nEnter 'quit' to end the program >>> ")

message = ""

while message != "quit":
    message = input(prompt)
        
    if message != "quit":
        print(message)


#

