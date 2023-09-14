"""
names = []

for _ in range(3):
    names.append(input("what's your name? \n"))

for name in sorted(names):
    print(f"Hello, {name}")
"""    


"""
name = input("What's your name? \n")

#with will automatically close the file for us, it is used with as file:
with open("names.txt", "a") as file: #"a" is for append, "w" will rewrite every time we open the file
    file.write(f"{name}\n")
"""

"""
with open("names.txt") as file:
    for line in file:
        print("Hello, ", line.rstrip()) #rstrip() removes the trailing characters.
"""

#program will sort alphabetically the content of the file
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
