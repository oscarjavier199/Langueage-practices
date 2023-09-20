print("Let's practice everything!") #prints message
print("You\'d need to know \'bout escapes with \\ that do: ") #prints message
print("\n newlines and \t tabs") #prints message

poem = """ #poem variable which contains a fragment of a poem
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") #prints -
print(poem) #prints poem
print("--------------") #prints -

five = 10 - 2 + 3 - 6 #variable five created to which we assign arithmetic operations
print(f"This should be five: {five}") #print message 

def secret_formula(number): #here we define a function with one parameter (number)
    jelly_beans = number * 500 #new variable = started multiplied by 500
    jars = jelly_beans / 1000 #new variable jars = jelly_beans / 1000
    crates = jars / 100 # new variable crates / 100
    return jelly_beans, jars, crates #here we return the previous variables

start_point = 10000 #new variable with a value of 10000
beans, jars, crates = secret_formula(start_point) #we set beans, jars, crates = to the function secret_formula with argument start_point which is = to 10000
print("With a starting point of: {}".format(start_point)) #print message
print(f"We'd have {beans} beans, {jars} jars, {crates} crates.") #prints message

start_point = start_point / 10 #start_point which is set 10000 is / by 10 so it can print all the decimal numbers we need

print("We can also do that this way:") #prints message
formula = secret_formula(start_point) #formula is = secret_formula which is equal to variables jelly_bans, jars and crates
print("We'd have {} beans, {} jars, {} crates.".format(*formula)) #prints message
    