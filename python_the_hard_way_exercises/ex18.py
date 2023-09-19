#this program will show how to define a variable and how to pass arguments and call 
#the function when we're done.


#this function is like the argv function in previous problems:
def print_two(*args): #*args: (asterisk args) 
    arg1, arg2 = args
    print("arg1: %r, arg2: %r " % (arg1, arg2))
#What does the * in *args do?
#That tells Python to take all the arguments to 
#the function and then put them in args as a list. 
#It’s like argv that you’ve been using, but for functions. 
#It’s not normally used too often unless specifically needed.


#we didn't have to use the *args, we can do the following:
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    
#this takes only one argument:
def print_only_one(arg1):
    print("arg1: %r" % (arg1))
    
#this takes no arguments:
def no_arg():
    print("I got nothin'")
    
#here we call all the 4 function we created to print the messages.
print_two("oscar", "perez")
print_two_again("oscar", "perez")
print_only_one("First")
no_arg()
