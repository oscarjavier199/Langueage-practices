#print the numbers from 1 to 20 inclusive:
numbers = []

for number in range(1, 21):
    numbers.append(number)
print(numbers)

#same code but in one line:
numbers = [number + 1 for number in range(0, 20)]
print(numbers)
