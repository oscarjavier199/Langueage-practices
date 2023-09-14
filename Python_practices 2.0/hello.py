# program asks you for your name and then says hello + your name
def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"): #function defined
    return f"hello, {to}"


if __name__ == "__main__": 
    main()