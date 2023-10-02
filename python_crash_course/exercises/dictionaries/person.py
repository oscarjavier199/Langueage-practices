#program to show how a dict can be used to store peoples information
#and how we can access that information 

person = {
    'first_name': 'Alex',
    'last_name': 'andersen',
    'age': 28,
    'city': 'munich',
}

person_1 = {
    'first_name': 'Oscar',
    'last_name': 'perez',
    'age': 23,
    'city': 'Bogota',
}

person_2 = {
    'first_name': 'charlie',
    'last_name': 'sheen',
    'age': 50,
    'city': 'New york',
}

first_name = person['first_name']
last_name = person['last_name']
age = person['age']
city = person ['city']

people = [person, person_1, person_2]

for human in people:
    if human == person:
        print('My good friend!')
    if human == person_1:
        print(f"I think I know you really good!")
    if human == person_2:
        print(f"Don't think I remember you that well to be honest")
    print(f"{human}\n")