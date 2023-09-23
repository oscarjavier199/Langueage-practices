#program will loop through given numbers until the condition is false:

#! creating function 
def while_function():
    i = 5 #sets value of i to 5
    numbers = []  #empty list to store results

    while i < 16: #while loop, will iterate through i until its value is less than a #
        print(f"At the top i is: {i}")#prints message
        numbers.append(i) #adds the new values of i to the 'numbers' list
    
        i = i + 1 #increases i by 1 each time the loop starts and goes through i
    
        #prints message
        print("Numbers now: ", numbers)
        print(f'At the bottom i is {i}')
        
    print("The numbers: ") #prints message

    for num in numbers: #for loop to iterate through the 'numbers' list and print its elements
        print(num)
        
while_function() #calling main function


#same exercise but an argument is passed to the function:
'''
#same exercise but an argument is passed to the function:
def while_function(digit):

    numbers = []  #empty list to store results

    while digit < 16: #while loop, will iterate through i until its value is less than a #
        print(f"At the top i is: {digit}")#prints message
        numbers.append(digit) #adds the new values of i to the 'numbers' list
    
        #digit += 8 #increases i by 1 each time the loop starts and goes through i
        digit += 4
        #prints message
        print("Numbers now: ", digit)
        print(f'At the bottom i is {digit}')
        
    print("The numbers: ") #prints message

    for num in numbers: #for loop to iterate through the 'numbers' list and print its elements
        print(num)
        
while_function(0) #calling main function
'''


#same exercise but using a for loop:
'''
numbers = []
for i in range(0, 19):
    numbers.append(i)
    print(f'numbers is: {numbers}')

'''
