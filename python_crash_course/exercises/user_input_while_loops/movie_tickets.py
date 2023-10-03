
prompt = "Please enter your age: "
prompt += ">>> "

active = True

while active:
    user_age = int(input(prompt))
    if user_age <= 3:
        print("Your ticket is free!")
        active = False
    elif user_age <= 12:
        print("Your ticket is $10")
        active = False
    else:
        print("The ticket is $15")
        active = False


