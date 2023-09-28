#program will count from 1 to 1 million
'''
numbers = []

for number in range(1, 1000001):
    numbers.append(number)
print(numbers)
'''

#using lists comprehension:
numbers = [number + 1 for number in range(0, 1000000)]
print(numbers)