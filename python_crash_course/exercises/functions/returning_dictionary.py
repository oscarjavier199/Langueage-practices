#program will return arguments as a dictionary:

def human(first_name, last_name, occupation=None):
    
    human_name = {'first': first_name, 'last': last_name}
    if occupation:
        human_name['occupation'] = occupation
    return human_name

human_full_name = human('jack', 'sparrow', occupation='pirate')
print(human_full_name)
