#program asks user for x and y int values and gives the result of the addition
#x = int(input("what's X?\n"))
#y = int(input("what's Y?\n"))
#print("Answer:", x + y)

#one line of code:
#print(int(input("What's X? ")) + int(input("What's Y" ))) #not recommended since it's harder to read/understand the code


#program takes 2 floats and rounds them to an int
#x = float(input("What's X?\n"))
#y = float(input("What's Y?\n"))
#z = round(x + y) #rounds the given numbers
#print(f"Answer: {z:,}") #formats the string to add a comma


#program takes 2 floats and divides them, then rounds them to an int
x = float(input("What's X?\n"))
y = float(input("What's Y?\n"))
z = x / y
print(f"Answer: {z:.2f}") #we want to print only 2 digits

