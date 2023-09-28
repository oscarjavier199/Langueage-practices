#print odd numbers using lists and a for loop:
odd_numbers = []

for odd in range(1, 21, 2):
    odd_numbers.append(odd)
print(odd_numbers)


#using lists comprehension:
numbers = [odd for odd in range(1, 21, 2)]
print(numbers)