#remove all occurances of a repeated value from a list:

pets = ['dog', 'dog', 'goldfish', 'cat', 'rabbit', 'dog']

print(f"list with original values:", pets)

while 'dog' in pets:
    pets.remove('dog')
print(f"List with removed values: ", pets)