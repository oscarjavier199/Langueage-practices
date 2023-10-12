from pathlib import Path

path = Path('guest.txt')

name_input = input("\nPlease write your name >>> \n")
path.write_text(name_input)