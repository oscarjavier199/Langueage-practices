from sys import argv #imports argv from sys library

print("How old are you?", end=' ') #prints message
age = input() #takes input from user
print("How tall are you?", end=' ') #prints message
height = input() #takes input from user
print("How much do you weigh?", end=' ') #prints message
weight = input() #takes input

print(f"So, you're {age} old, {height} tall and {weight} heavy.\n") #prints message with formatting

#takes arguments from user
"""
script, filename = argv
txt = open(filename)

print("Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
"""
#prints message
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes')
print("with \\ that do \n newlines and \t tabs.")

#assigns poem to poem variable
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

#prints message
print("--------------")
print(poem)
print("--------------")

#creates variable five with arithmetic operations
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}") #prints message

#creates function with one argument
def secret_formula(started):
    jelly_beans = started * 500 #creates variable 
    jars = jelly_beans / 1000 #new variable stores the result of previous variable / by 1000
    crates = jars / 100 #new variable stores the result of previous variable / by 100
    return jelly_beans, jars, crates #returns variables


start_point = 10000 #new variable = 10000
beans, jars, crates = secret_formula(start_point) #assigns variables from function secret_formula = 10000(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point)) #prints message with formatting
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.") #prints message with different form of formatting

start_point = start_point / 10 #sets start_point = to start_point / 10 to get decimals

print("We can also do that this way:")
formula = secret_formula(start_point) #sets variable formula = secret_formula variables, without the argument(start_point), we'd get an error (str.format() argument after * must be an iterable, not function)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


#variables
people = 20
cats = 30
dogs = 15

#if functions
if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

#increases dogs by 5
dogs += 5

#if arguments
if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people >= dogs:
    print("People are dogs.")
