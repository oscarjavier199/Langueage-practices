#program will take a greeting as input from user
#if the input is hello it will print $0
#if the input starts with "h" but is not hello will print $20
#any other greeting will print $100

def main():
    greeting()
    
def greeting():
    greet = input("Greetings: ")
    
    if greet.capitalize() == "Hello":
        print("$0")
    elif greet.startswith("h") or greet.startswith("H"):
        print("$20")
    else:
        print("$100")
        
if __name__ == "__main__":
    main()
