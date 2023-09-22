#here we will create a mapping of state to abbreviation:
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA', 
    'New york': 'NY',
    'Michigan': 'MI'
}

#here we will create a basic set of states and some cities in them:

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#here we will add some cities:
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("Ny State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan abbreviation is: ", states['Michigan'])
print("Florida abbreviation is: ", states['Florida'])

#accessing the state then cities dict
print('-' * 10)
#here we will access the value of 'Detroit' in the dict cities by accessing two lists, cities and states.
print("Michigan has: ", cities[states['Michigan']]) #first we look for 'Michigan' in dict states, 'Michigan':'MI', then it will look for 'MI' in cities dict, which is = to 'MI':'Detroit', output: "Michigan has: Detroit"
print("Florida has: ", cities[states['Florida']]) 

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()): #The items() method in Python is used to return a view object that contains the key-value pairs of a dictionary
    print(f"{state} abbreviated is: {abbrev}")

#prints every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'{abbrev} has the city {city}')

#now we will print the both previous statements into one
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

## safely get a abbreviation by state that might not be there
print('-' * 10)
state = states.get('Kansas')

if not state:
    print("Sorry, no Kansas.")
    
# get a city with a default value
city = cities.get('KS', 'Does Not exist')
print(f'The city for the state "KS" is: {city}')

