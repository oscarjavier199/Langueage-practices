#program will open a file using the open() command and we will be able to read it,
#we need to provide the name of the file, for this exercise the file is called
#ex15_sample.txt

#import argv from sys
from sys import argv

#assign two variables to argv
script, filename = argv

#create a variable called txt and use the open() command which opens a file
txt = open(filename)

#prints a message and the name of the file
print("Here's your file %r:" %(filename))

#prints the content of the file (only to read it)
print(txt.read())

"""
#prints a message
print("Type the filename again:")

#create a new input variable with a str ">"
file_again = input(">")

# create variable txt_again to open a file again
txt_again = open(file_again)

#prints the content of the file
print("txt_again.read()")
"""