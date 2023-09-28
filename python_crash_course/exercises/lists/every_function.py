#program will use every function
# introduced in chapter 3 of book python crash course 3rd edition.

cities = ['munich', 'oslo', 'copenhagen', 'berlin', 'reykjavik', 'sydney']

cities.append('madrid')
cities.insert(1, 'barcelona')
print(f'Travel list: {cities}\n')

cant_visit = cities.pop()
cant_visit_2 = cities.pop(1)
print(f'''sorry, two cities are not available due to weather conditions: {cant_visit} and {cant_visit_2} are no longer available\n''')

del cities[5]
print(f'I changed my mind I only want to visit the following cities: {cities}\n')

cities[3] = 'uppsala'
print(f"Fine then I'll add a new city! {cities[3]}\n")

cities.sort()
print('cities sorted in alphabetical order:', cities)

cities.sort(reverse=True)
print('reversed order:', cities)

print('sorted: ', sorted(cities))

print('sorted in reverse:', sorted(cities, reverse=True))

cities.reverse()
print('reverse it!',cities)

print('How many cities are on my list?\n', len(cities))