#program asks user for x and y int values and gives the result of the addition
"""""
x = int(input("what's X?\n"))
y = int(input("what's Y?\n"))
print("Answer:", x + y)
"""

#one line of code for previous code:
"""""
print(int(input("What's X? ")) + int(input("What's Y" ))) #not recommended since it's harder to read/understand the code
"""

#program takes 2 floats and rounds them to an int
"""""
x = float(input("What's X?\n"))
y = float(input("What's Y?\n"))
z = round(x + y) #rounds the given numbers
print(f"Answer: {z:,}") #formats the string to add a comma
"""

#program takes 2 floats and divides them, then rounds them to an int
"""""
x = float(input("What's X?\n"))
y = float(input("What's Y?\n"))
z = x / y
print(f"Answer: {z:.2f}") #format indicates that we only want to print only 2 digits
"""

#program asks user for x and y int values and gives the result of the division
'''
x = int(input("what's X?\n"))
y = int(input("what's Y?\n"))
print("Answer:", x / y)
'''

#program returns the squared value of a given number
def main(): #defining a function
    x = int(input("What's X?\n")) #asks user for input
    print("X squared is", square(x)) #gives user the answer
    
def square(n): #defines square function
    return n * n #returns the squared value

main() #calling main function to know the square value of a given number