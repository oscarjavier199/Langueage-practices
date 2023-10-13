from pathlib import Path
import json

# program verifies if a username is stored in json file
# if it is it greets user, if its not, it prompts user for name
# and stores it in json file

path = Path('username.json')

if path.exists():
    content = path.read_text()
    stored_name = json.loads(content)
    print(f"Welcome back {stored_name}")

else:
    name = input("\nWhat's your name >>> ")
    content = json.dumps(name)
    path.write_text(content)
    print(f"We'll remember you next time {name}! \n")