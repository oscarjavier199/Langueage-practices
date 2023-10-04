while True:
    age = input("Please enter your age: ")
    age = int(age)
    if age < 5:
        print("Your ticket is free!")
        break
    elif age < 15:
        print("Your ticket is $12")
        break
    else:
        print("Your ticket is $50")
        break
    
"""
ticket_flag = True

while True:
    age = input("Please enter your age: ")
    age = int(age)
    if age < 5:
        print("Your ticket is free!")
        ticket_flag = False
    elif age < 15:
        print("Your ticket is $12")
        ticket_flag = False
    else:
        print("Your ticket is $50")
        ticket_flag = False
"""