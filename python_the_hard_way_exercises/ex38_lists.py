ten_things = 'Apples Oranges Crows Telephone Light Sugar' #variable with a str

print("List with 10 elements: ", ten_things) #prints message
print("""...
Wait there are not 10 thing in that list. Let's fix that""")

stuff = ten_things.split(' ') #new variable equal to ten_things list, .split will split the str where there are any whitespaces.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] #list

while len(stuff) != 10: #while loop, len will get the length of stuff which is equal the ten_things str
#the while loop will be executed until the items in stuff are 10
    next_one = more_stuff.pop() #removes one element from specified list (more_stuff) in this case.
    print("Adding: ", next_one) #prints message
    stuff.append(next_one) #appends the item that was .pop() 'removed' from next_one ='more_stuff' list
    print(f"There are {len(stuff)} items.now.") #prints message, len(stuff) will get the length of stuff

print("There we go: ", stuff) #prints message
print("Let's do some things with stuff :)") #prints message

print(stuff[1]) #prints the 1st item in the list, not the 0, the first
print(stuff[-1]) #prints the last item of the list
print(' '.join(stuff)) #The join() method takes all items in an iterable (stuff) and joins them into one string.
print('#'.join(stuff[3:5])) #prints the 3rd item of the str which in ordinal numbers would be the 4th item and the 4th item
#and join will "join" them with the specified symbol #