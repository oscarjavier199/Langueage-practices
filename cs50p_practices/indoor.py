#program will ask user for an input in uppercase and then return the same input but in lowercase
def main():
    hello()
    
def hello():
    say_something = input("please type something in uppercase! \n") #asks for input
    print(say_something.lower()) #prints input and  .lower() converts it in lowercase

if __name__ == "__main__":
    main()
