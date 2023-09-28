numbers = []

for number in range(1, 11):
    numbers.append(number ** 3)
print(numbers)


#using list comprehension:
third_power = [numbers ** 3 for numbers in range(1, 11)]
print(third_power)