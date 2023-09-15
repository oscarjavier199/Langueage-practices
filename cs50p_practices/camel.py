def main():
    snake_case()
    
def snake_case():
    camel_case_input = input("camelCase: ")
    print("snake_case: ", end="") #end will avoid the answer appearing in a new line

    for camel in camel_case_input: #loop to iterate through user answer
        if camel.isupper(): #is.upper checks for uppercase letters
            print("_" + camel.lower(), end="") #.lower prints any uppercase in lowercase
        else: 
            print(camel, end="") #end="" is to print from right to left and not in a new line
    print() #to leave a new space after previous print statement
    
if __name__ == "__name__":
    main()