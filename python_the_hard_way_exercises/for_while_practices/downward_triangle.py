#variable wich will set the rows of the triangle to 10
rows  = 10

#loop iterates over a range of numbers from rows + 1 to 0, with a step of -1
#this means the loop will run 11 times, with the variable row decreasing by 1 each time.
for row in range(rows + 1,  0,  -1):
    
#the variable space will inclrease by 1 each iteration, this inner loop will run 10 times, 
#with space going from 0 to 9
    for space in range(0, row - 1):
        
#this line prints a hash symbol followed by a space using the end='' parameter to prevent a 
#new line from being printed, the number of hash symbols printed on each row will decrease by 1 as row decreases.
        print("# ", end=" ")
        
# The fifth line prints an empty string, which causes a new line to be printed.    
    print("")
