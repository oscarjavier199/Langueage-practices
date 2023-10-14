from pathlib import Path
import json

def favorite_number(path):
    '''Asks user for favorite number'''
    
    number = input('''\nwhat's your favorite number? 
ENTER "q" to quit \n\n>>> ''')
    if number == 'q':
        quit
    else:
        path = Path('fave_number.json')
        contents = json.dumps(number)
        path.write_text(contents)

def verify_if_exists(path):
    '''verifies if number is already stored'''
    
    path = Path('fave_number.json')
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        print(f"\nStored Number: {number}\n")
    else:
        return None

def read_fave_number(path):
    '''if number is stored will print it'''
    
    path = Path('fave_number.json')
    contents = path.read_text()
    number = json.loads(contents)
    print("\nReading from JSON file... \n")
    print(f"your favorite number is {number}")

verify_if_exists(Path)
favorite_number(Path)
read_fave_number(Path)
