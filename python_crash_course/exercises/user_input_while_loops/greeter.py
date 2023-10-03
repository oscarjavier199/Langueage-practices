#simple input() program
'''
hello = input("What\'s your name?\n")
print(f"Nice to meet you, {hello}")
'''
# assign a message to a variable and then pass it to input
prompt = '''If you share your name, we can personalize the messages you see.
What is your first name? '''
name = input(prompt)
print(f"Nice to meet you {name}")

#take an int as input using int()
age = int(input("\nHow old are you? "))
print(f"Your age: {age}")

#we can also use this method to accept an int as input
age_1 = input('\nhow old are you? ')
age_1 = int(age)
print(f'I get it you\'re {age_1}')

#