#alphabetical order
cars = ['porsche', 'bmw','ferrari', 'tesla', 'maserati']
cars.sort()
print(cars)

#reverse-alphabetical order
cars_2 = ['mazda', 'volkswagen', 'lamborghini', 'chevrolet', 'renault']
cars_2.sort(reverse=True)
print(cars_2)

#sorted()
print(f'This is the original list: \n{cars_2}')
print(f'this is the sorted list:\n{sorted(cars_2)}')

#reverse()
motorcycles = ['ninja', 'suzuki', 'bmw']
motorcycles.reverse()
print(f'Reversed order:\n {motorcycles}')

#finding the length of a list suing len()
print(len(motorcycles))
