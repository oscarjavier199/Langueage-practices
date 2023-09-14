#program will take input from user (str) and then return the same input
# but replace any whitespace with ...(three periods)

def main():
    user_input()
    
def user_input():
    user_says = input("Please type something! \n") #takes input
    print(user_says.replace(" ", "...")) # .replace() will replace the given argument in position 0 with the argument in position 1
    
if __name__ == "__main__":
    main()