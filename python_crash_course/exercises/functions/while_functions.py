#using while in a function to get input from user:

def user(first_name, last_name):
    
    person = f'{first_name} {last_name}'
    return person

while True:
    print("\nEnter your name please")
    print("(Enter 'q' if you want to quit)")
    
    name = input("\nFirst name: ")
    if name == 'q':
        break
        
    l_name = input("\nLast name: ")
    if l_name == 'q':
        break
    
    user_name = user(name, l_name)
    print(f'\n{user_name}')