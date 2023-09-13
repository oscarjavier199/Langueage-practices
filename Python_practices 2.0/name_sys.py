import sys

#argv will print the arguments given by user but we need to manage how many arguments the program will accept

# sys.argv program
'''
try:
    print("Hello, my name is", sys.argv[1]) #the name of the file is in position [0] that's why we need [1]
except:
    print("Please enter your name")
'''
    
#other option for the program
'''
if len(sys.argv) < 2: #if user enters no arguments will print next line
    print("Too few arguments")
elif len(sys.argv) > 2: #if user enters more than one argument will next line
    print("too many arguments")
else: #if user enters just one argument (first name) will print next line
    print("Hello, my name is", sys.argv[1])
'''    

#sys.exit will print the string and then exit the program earlier
'''
if len(sys.argv) < 2: 
    sys.exit("Too few arguments") #if user inputs no arguments the program will print message and then exit
elif len(sys.argv) > 2:  
    sys.exit("too many arguments")#if user inputs more than 1 argument (besides the name of the program [0]) the program will print message and then exit
    
print("Hello, my name is", sys.argv[1]) #if user inputs just one argument the program will print message and then exit
'''

#slicing an output
if len(sys.argv) < 2: 
    sys.exit("Too few arguments") 
    
for arg in sys.argv[1:]: # [1:] is to slice the output we get, without it we would get also the name of the program, if we want to slice an argument at the end it would be [1:-1]
    print("Hello, my name is", arg) 