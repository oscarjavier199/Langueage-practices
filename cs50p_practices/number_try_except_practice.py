#program will return the value of x, but if user's input is not an int the while loop will keep asking user to enter an int

def main():
    x = get_int("What's x? ")
    print(f"X is {x}")
    
def get_int(prompt):
    while True: #while loop will keep asking user to enter an int
        try:
            return int(input(prompt)) #if user enters a value that is not an int it would've raised a value error, that's why we need line 10 and 11
        except ValueError: 
            print("Please enter a number, X is not an integer")

main()
