def main():
    hello("World")
    goodbye("world")
    
def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__": #if we import this file as a module into other file, the final call to main will be ignored
    main()
