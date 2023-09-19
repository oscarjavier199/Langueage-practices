#import library
from sys import argv

#give two arguments to argv
script, input_file = argv


#defining a function with one argument(f) 
"""This function will print the whole file """
def print_all(f):
    print(f.read()) #The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
    

#defining another function with one argument(f)
"""This function will change the position back to the beginning of the file"""
def rewind(f):
    f.seek(0) #seek() function is used to change the position of 
    #the File Handle to a given specific position. File handle is like a cursor,
    #which defines from where the data has to be read or written in the file. 
    

#function with two arguments, 
"""This function will print 3 lines"""
def print_a_line(line_count, f):
    print(line_count, f.readline()) #f.readline() reads one entire line from the file. 
    

current_file = open(input_file) #open(input_file) will open the file given by the user


print("First let's print the whole file:\n") #print message
print_all(current_file) # here we call the function print_all defined on line 7 which will 
#print the whole content of the file


print("now let's rewind, kind of like a tape.") #prints message
rewind(current_file) #calls function rewind, defined in line 12, it will change the position back to 0 (the beginning of the file)


print("Let's print three lines:") #prints message
current_line = 1 #we create the variable current_line which is = to 1, it means we will read the file from line 1
print_a_line(current_line, current_file) #we call the function print_a_line which will print one line of the file.

current_line = current_line + 1 # increases current_line + 1 so it can print the second line of the file
print_a_line(current_line, current_file) #calling the function (current_file) is the file given by the user

current_line = current_line + 1 #increases current_line again + 1 so it prints the 3 line of the file
print_a_line(current_line, current_file) #calling the function