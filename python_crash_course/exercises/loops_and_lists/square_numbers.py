#empty list to store results
squares = []
#loop that iterates from 1 to 21
for value in range(1, 21):
#appends value ** 2 to the squares list
    squares.append(value**2)
#prints result
print(squares)
print('-' * 20)

#program prints range (1, 21) ** 2 in fewer lines
squares = []
for value in range(1, 21):
    squares.append(value ** 2)
print(squares)
print('-' * 20)

#program prints range (1, 21) ** 2 in only one line
squares = [value ** 2 for value in range(1, 21)]
print(squares)