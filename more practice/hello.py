# program asks you for your name and then says hello + your name

def hello():
    name = input ("what's your name? \n").strip().title() #asks user for name
    home = input ("where are you from " + name + "? \n").strip().title() #asks user where is him/her from
    print('A pleasure to meet you, {}!'.format(name), f'from {home}') #greets user
    
    
hello()
     