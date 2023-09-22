#lists and dicts comparison

#! list
#to get an element in a list we have to use numbers
things = ['a', 'b', 'c', 'd', 'e'] #define lists
print('list:')
print(things[1]) #prints the second element of the list

things[1] = 'z' #replaces the second item of the list for 'z'
print(things)#prints the list with replaced value

#here we will see how to access the value of a dict using its key:
print('Dict:')


#! dictionary:
stuff = {'name': 'oscar', 'age': 23, 'height':6 * 12}

#prints name out of dictionary using its key
print("Name:", stuff['name'])

#prints Age out of dictionary using its key
print("Age:",stuff['age'])

#prints Height out of dictionary using its key
print("Height:",stuff['height'])

#assigns the key city and value NY to dict
stuff['city'] = 'NY'

##prints city out of dictionary using its key
print("City:",stuff['city'])

#We can also put new things into the dictionary 
#with strings. It doesn’t have to be strings, though. We can also do this:
stuff[1] = 'Wow'
print(stuff)

#we can also delete things from a dict suing the #! del
#keyword 
del stuff["city"]
del stuff[1]
print(stuff)
