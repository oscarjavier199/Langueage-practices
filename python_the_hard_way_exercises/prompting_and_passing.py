from sys import argv #import argv to take input from user in command line


#program will ask some questions about the user

script, user_name = argv #giving two arguments to argv
prompt = "howdy? " # prints in the terminal the > symbol to signal the answer of user

print("hi %s, I'm the %s script." % (user_name, script)) #prints the message and the name entered by user
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % (user_name)) 
likes = input(prompt) #stores the answer from user in the variable likes, will make it
#easier if we need the answer from the user later on.

print("Where do you live %s" % (user_name))
lives = input(prompt) #stores the answer from user in the variable live, to use it later if needed

print("what kind of computer do you have?")
computer = input(prompt) #stores the answer from user in variable computer

print("""
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
and you have a %r computer. Nice!""" % (likes, lives, computer)) #here we use the answers stored in the previous variables.