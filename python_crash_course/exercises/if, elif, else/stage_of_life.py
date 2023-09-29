#program will ask user for his/her age and then print a message depending 
#in user's age

print("please enter your age:")
age = int(input())

if age < 2:
    print("You're a baby 👶")
if age == 2 or age < 4:
    print("You're a toddler 🧒")
if age == 4 or age < 13:
    print("You're a kid 🥳")
if age == 13 or age < 20:
    print("You're a teenager 🤪")
if age == 20 or age < 65:
    print("You're an adult👨")
if age >= 65:
    print("You're an elder👴👵")