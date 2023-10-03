'''
prompt = "\nTell me something and I'll repeat it back to you"
prompt += "\nEnter 'quit' to end the program >>> "

#variable message to keep track of whatever value the user enters
message = "" 

while message != 'quit':
#Whatever the user enter is assigned to message
    message = input(prompt)
#without this if statement the program would also return 'quit as output for user'
    if message != 'quit':
        print(message)
'''
print("*" * 25)

#!USING FLAG VARIABLE
prompt = "\nTell me something and I'll repeat it back to you"
prompt += "\nEnter 'quit' to end the program >>> "

# active is the flag set to True
active = True

while active:
    message = input(prompt)
    if message == 'quit':
#flag is set ot false, so if user's imput is 'quit, the program will stop.
        active = False
#if user's input is not 'quit', else block will execute.
    else:
        print(message)
