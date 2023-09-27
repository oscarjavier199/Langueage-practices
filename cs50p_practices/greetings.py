# program asks you for your name and then says hello + your name
def main():
    hello()

def hello(): #function defined
    name = input ("what's your name? \n").strip().title() #asks user for name, (strip)removes whitespace from str and (title)capitalizes first letter
    home = input ("where are you from " + name + "? \n").strip().title() #asks user where is him/her from, (strip)removes whitespace from str and (title)capitalizes first letter
    print(f"A pleasure to meet you, {name}!", f"from {home}") #greets user (f is for format)
    
if __name__ == "__main__": 
    main()
