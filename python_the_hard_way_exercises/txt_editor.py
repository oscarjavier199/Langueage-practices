from sys import argv #import argv

script, filename = argv #assign arguments to argv

print("We're going to erase %r." %(filename)) #print message
print("If you don't want that, hit CTRL-C (^c).") #print message
print("If you do want that, hit RETURN.") #print message
 
input("?") #print message

print("Opening the file...") #print message
target = open(filename, "w") #open the file in write mode

print("Truncating the file.   Goodbye!") #print message
target.truncate() #erase the content of the file

print("Now I'm going to ask you for three lines") #print message

line1 = input("line 1: ") #ask for input
line2 = input("line 2: ") #ask for input
line3 = input("line 3: ") #ask for input

print("I'm going to write these to the file.") #print message

target.write(line1) .write(), #will write the input entered in line 1 to the document
target.write("\n") 
target.write(line2) #will write the input entered in line 2 to the document
target.write("\n")
target.write(line3) #will write the input entered in line 3 to the document
target.write("\n")

print("And finally, we close it.")
target.close()  #safely closes the program