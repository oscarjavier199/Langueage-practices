#remake of the program pizza_toppings.py in a different way using break variable
'''
prompt = "\nPlease enter the toppings you want in your pizza: "
prompt += ">>> "
print("Enter 'quite' to finish your order")

while True:
    message = input(prompt)
    if message != 'quit':
        print(f"{message} added to your pizza!")
    else:
        break
        
print("\n\tYour pizza will be ready in 15 minutes!\n")
'''

#remake of program movie_tickets using only conditional statements
prompt = "Please enter your age: "
prompt += ">>> "

user_age = 1

while user_age == 1:
    user_age = int(input(prompt))
    user_age += 1
    if user_age <= 3:
        print("Your ticket is free!")
    elif user_age <= 12:
        print("Your ticket is $10")
    else:
        print("The ticket is $15")
