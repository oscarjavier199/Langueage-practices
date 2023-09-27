#modifying an element of a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print('old list:', motorcycles)

motorcycles[0] = 'ducati'
print('new list:', motorcycles)

#append an item to the end of a list
motorcycles.append('Ninja')
print('after appending an item:', motorcycles)


print('-' * 20)

#appending elements to an empty list
cars = []
cars.append('Porsche')
cars.append('Ferrari')
cars.append('Maserati')
cars.append('Mazda')
print('New list:', cars)

#inserting an item using .insert() we insert lamborghini to position (1)
cars.insert(1, 'Lamborghini')
print('inserting an item:', cars)

#removing an item using the del statement
del cars[3]
print('item removed: ', cars)

#removing an item using pop()
popped_cars = cars.pop()
print('An item was popped:', popped_cars)
print('new cars list:', cars)

#popping an item at any given position
fave_cars = cars.pop(0)
print(f'My favorite car brand is {fave_cars.title()}.')