import random

#coin toss (random.choice)
'''
coin = random.choice(["Heads", "Tails"]) #choice Returns a random element from the given sequence
print(coin)
'''

#random number (random.randint)
'''
number = random.randint(1, 10) #The randint() method returns an integer number selected element from the specified range.
print(number)
'''

#shuffle cards (random.shuffle)

cards = ["Jack", "Queen", "King"]
random.shuffle(cards) #	shuffle() Takes a sequence and returns the sequence in a random order
for card in cards:
    print(card)



