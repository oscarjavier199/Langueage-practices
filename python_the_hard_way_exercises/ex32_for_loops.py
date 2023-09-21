#here we define 3 lists
the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "orange", "pear", "apricot"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#this for loop goes through the (the_count list)
for number in the_count:
    print(f"This is count {number}")

#another for loop that goes through the elements in the "fruits" list
for fruit in fruits:
    print(f"This is a fruit: {fruit}")

#for loop that goes through every element in the 'change' lis
for money in change:
    print(f"I got: {money}")

#empty list:
elements = []

#for loop to add elements from range 0,6, which would be 0 to 5, to the elements list.
for i in range(0, 6): #range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
    print(f"Adding {i} to the list.")
    #append is a function to add a new element to the end of a list
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

