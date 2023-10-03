prompt = "\nPlease enter the toppings you want in your pizza: "
prompt += ">>> "
print("Enter 'done' to finish your order")

active = True

while active:
    user_input = input(prompt)
    if user_input == 'done':
        active = False
    else:
        print(f"{user_input} added to your pizza!")
        
print("\n\tYour pizza will be ready in 15 minutes!\n")