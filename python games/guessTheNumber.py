#This is a Guess the Number Game.

#importing the random module so the program calls the randint() function
#which will come up with a random number for the player to guess
import random

#variable guessesTaken 
#we'll store the number of guesses the player has made in this variable
guessesTaken = 0
print('Hello! What is your name? ') #print message
myName = input() #takes input from user and store it in myName

#here we call the function randint(1, 30) and stores the return value in 'number'
number = random.randint(1, 30)
print('Well, ' + myName + ', I am thinking of a number between 1 and 30')

#loop will iterate 6 times
for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high')
    if guess == number:
        break
    
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')