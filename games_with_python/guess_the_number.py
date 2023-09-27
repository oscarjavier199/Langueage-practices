# this is a guess the number game

#imports random module
import random

#variable set = 0
guessesTaken = 0

#prints message and takes input
print('Hello! what is your name? ')
myName = input()

#generates random number from specified range (0, 50)
number = random.randint(1, 50)
print(f'Well, {myName}, I am thinking of a number between 1 and 50.')

#iterates only range(15) times
for guessesTaken in range(15):
    print('Take a guess.')
    guess = input()
#takes input and converts it into an int, The string you pass to must be made of numbers.
    guess = int(guess)
#if, elif, else statements
    if guess < number:
        print('Your guess in too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        break
#if user enters the right number
if guess == number:
    print(f'Good job {myName}! You guessed my number in {guessesTaken} guesses')
    
#if user doesn't enter the right number
else:
    number = str(number)
    print(f'Nope, the number I was thinking of was {number}.')