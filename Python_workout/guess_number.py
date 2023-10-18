from random import randint

def guessing_game():
    
    '''Guessing number program'''
    
    print("\nLet's play a game called guess the number...")
    print("\n\tInstructions:\n\nI'll think of a random number between 10 and 30")
    print("Then you will give me a number\n-If it's too low I'll tell you")
    print("-If it's too high I'll let you now\n\tYou have 5 tries\n")
    
    max_attempts = 5
    attempts = 0
    number = randint(10, 30)
    
    while attempts < max_attempts:
        
        try:
            user_number = int(input("Enter your number... "))
            if user_number == number:
                print("You Won! That's the number!")
                break

            if user_number < number:
                print("Too low, try again \n")

            if user_number > number:
                print("Too high try again \n")
                
        except ValueError:
            print("\n\t--- Sorry, enter only numeric values ---\n")
            
        if user_number == max_attempts:
                print("Sorry no more tries for you 🤐")
                break

guessing_game()