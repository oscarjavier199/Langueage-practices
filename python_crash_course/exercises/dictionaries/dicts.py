#printing key-values from a dictionary
cities_countries = {
    'oslo': 'norway', 
    'munich': 'germany',
    'bogota': 'colombia',
}
for country in cities_countries.values():
    print(f"{country}")
print("*" * 20)

#adding a key-value to a dictionary
movies = {}
movies['Harry Potter'] = 'the chamber of secrets'
print(movies)
print("*" * 20)

# for loops in dictionaries
heroes = {
    'batman': 'Bruce Wayne',
    'superman': 'clark kent',
    'wonder woman': 'diana of themyscira',
    'green lantern': 'hal jordan'
}

for hero, identity in heroes.items():
    print(f"{hero.title()}'s real identity is {identity.title()} 😯")
print("*" * 20)

#accessing only the keys of the previous exercise
print("I only know these heroes:")
for key_hero in heroes.keys():
    print(f"{key_hero.title()}")
print('sorry not sorry!')

#accessing only the values from heroes{} dictionary
print("\nI KNOW WHO YOU ARE!")
for real_identity in heroes.values():
    print(f"{real_identity.title()}")
print("*" * 20)

#set() method to remove duplicated values
favorite_movie = {
    'person 1': 'harry potter',
    'person 2': 'narnia',
    'person 3': 'narnia',
    'person 4': 'brides maids',
    'person 5': 'I don\'t watch movies',
    'person 6': 'mission impossible',
    'person 7': 'mission impossible',
}
print("WE NEED TO REMOVE ALL DUPLICATE VALUES FROM THE POLL!!!")
print("...")
print("No worries I got you🧐")
for movie in set(favorite_movie.values()):
    print(f"{movie}")
print("*" * 20)

#sorted method
glossary = {
    'batman': 'justice league',
    'iron man': 'the avengers',
    'hulk': 'the avengers',
    'cyborg': 'justice league',
    'spiderman': 'the avengers',
    'constantine': 'justice league dark',
}
print("Please organize this glossary of heroes in alphabetical order! ")
print(glossary.keys())
print("...")
print("Considere it Done:\n")
for key_hero in sorted(glossary.keys()):
    print(f"{key_hero.title()}")
    
print("*" * 20)

#del method to delete key-values
del glossary['hulk']
print(f"{glossary}")
