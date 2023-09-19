

def cheese_and_crackers(cheese_count, boxes_of_crackers): #defining the function with two arguments (cheese_count, boxes_of_crackers)
    print("You have %r cheeses." % (cheese_count)) #print message
    print("You have %r boxes of crackers!" % (boxes_of_crackers)) #print message
    print("Man that's enough for a party")
    print("Get a blanket!")
    
#here we are outside the function:

print("We can just give the function numbers directly:") #print message
cheese_and_crackers(20, 30) #passing the numbers(20, 30) to arguments (cheese_count, boxes_of_crackers)from the cheese_and_crackers function.

print("OR, we can use variables from our script:") #print the message
amount_of_cheese = 10 #variable is created and we assign the number 10 to it
amount_of_crackers = 50 #variable is created and we assign the number 50 to it
cheese_and_crackers(amount_of_cheese, amount_of_crackers) #here we assign the two previous variables to the function cheese_and_crackers so they are passed to the two arguments (cheese_count, boxes_of_crackers)

print("We can even do math inside too:") #print message
cheese_and_crackers(10 + 20, 5 + 6) #here we specify that 10+20 is passed to the cheese_count argument and 5 + 6 is passed to boxes_of_crackers

print("And we can combine the two, variables and math:") #print message
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #amount_of_cheese = cheese_count + 100 and amount_of_crackers = boxes_of_crackers + 1000
