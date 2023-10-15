from pathlib import Path
import json

def users_name(path):
    '''Asks user for name, last name and country of residence'''
    user_info = {}
    
    while True:
        name = input("\nwhat's your name? ")
        l_name = input("\nWhat's your last name? ")
        country = input("\nWhere do you live? ")
        if name  == 'q':
            break
        else:
            user_info['Name']=name
            user_info['Last name']=l_name
            user_info['country']=country
            path = Path('user_info.json')
            user_info = json.dumps(user_info)
            path.write_text(user_info)
            break

def verify_if_exists(path):
    '''verifies if information is already stored'''
    
    path = Path('user_info.json')
    if path.exists():
        contents = path.read_text()
        user_information = json.loads(contents)
        print(f"\nStored Info: {user_information}\n")
    else:
        return None

def read_info(path):
    '''if information is stored will print it'''
    
    path = Path('user_info.json')
    contents = path.read_text()
    user_information = json.loads(contents)
    print("\nReading from JSON file... \n")
    print(f"We have this information about you: \n{user_information}")
    print("\nIs is correct or would you like to edit it? \n")
    edit = int(input("1. Edit or 2.It's fine\n >>> " ))
    if edit == 1:
        users_name(path)
        print(f"\nInformation updated!\nGoodbye!")
    if edit == 2:
        print("\nGreat, the information was stored! \n")


verify_if_exists(Path)
users_name(Path)
read_info(Path)
