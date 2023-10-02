#program to show how a dict can be used to store peoples information
#and how we can access that information 

person = {
    'first_name': 'Alex',
    'last_name': 'andersen',
    'age': 28,
    'city': 'munich',
}

first_name = person['first_name']
last_name = person['last_name']
age = person['age']
city = person ['city']

print(f"This person is called {first_name}")
print(f'{first_name}\'s last name is {last_name.title()}')
print(f'he is {age} years old')
print(f"And He is from {city.title()}")