# program asks you for your name and then says hello + your name

def greet_someone():
    name = input ("what's your name? ")
    home = input ("where are you from " + name + "? ")
    print('A pleasure to meet you, {}!'.format(name), f'from {home}')
    
greet_someone()
    