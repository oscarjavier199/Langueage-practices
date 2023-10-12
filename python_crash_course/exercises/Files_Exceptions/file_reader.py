#import pathlib and Path module
from pathlib import Path

# we assign the file to the module Path, so it can look for the file and assign
# it to the variable path
path = Path('pi_million_digits.txt')

# we then assign path to the variable contents to print the text of the file with
# read_text() method rstrip() will remove any withe spaces at the end of the file
contents = path.read_text().rstrip()



#empty string to hold the string that will be created
pi_string = ''

#iterate through each line and add it to previous empty string
#splitlines() separates the content of the file in lines
for line in contents.splitlines():
    pi_string += line.lstrip()
    
#print the new string and the length of the string
print(pi_string[:50])
print(len(pi_string))