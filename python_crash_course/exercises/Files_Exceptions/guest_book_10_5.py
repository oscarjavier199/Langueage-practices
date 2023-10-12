from pathlib import Path

path = Path('guest_book.txt')

saved_names = ''

while True:
    names = input("Please enter your a few names) >>> ")
    print("Enter 'end' to exit the program \n")
    saved_names += (f"{names}\n")

    if names != 'end':
        continue
    else:
        break
    
path.write_text(saved_names)

