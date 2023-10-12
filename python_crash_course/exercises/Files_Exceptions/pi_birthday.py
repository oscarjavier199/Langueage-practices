from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text().rstrip()

pi_string = ''

for line in contents.splitlines():
    pi_string += line.lstrip()
    
birthday = input("Enter your birthday in the format ddmmyy >>> ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of py 🥳")
else:
    print("Your birthday does not appear in the first million digits of py😪")
