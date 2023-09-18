#program will copy the information from one file (test.txt) to (test1.txt)

from sys import argv #imports argv 
from os.path import exists # exists will return True if a file exists

scrip, from_file, to_file = argv #takes arguments from user

print("Copying from %s to %s" % (from_file, to_file)) # prints message with given parameters


#we could do these two on one line:
#origin file
in_file = open(from_file) # opening the origin file 
indata = in_file.read()  # opening the origin file in read mode

print("The input file is %d bytes long" % (len(indata))) #len() will get the length of the file
print("Ready, hit Return to continue, CTRL-C to abort") # print message
input() #input from user

#destination file
out_file = open(to_file, "w") #assigning to_file to out_file variable to be opened in writing mode.
out_file.write(indata) # write the data to to_file which is the destination file.

print("Alright, all done.") #prints message

out_file.close() #closes file
in_file.close() #closes file