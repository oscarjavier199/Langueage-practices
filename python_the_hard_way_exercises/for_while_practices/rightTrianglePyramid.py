#evaluates the number of rwos we want to print
rows = 16

#this line controls the number of spaces before printing each hash
spaces = 2 * rows - 2

#for loop to iterate from 0 to rows(16)
for row in range(0, rows):
#loop iterates from 0 to spaces, prints a space for each iteration
    for space in range(0, spaces):
        print(end=" ")
        
#decrements the value of spaces by 2, so that the next row will have two fewer spaces
    spaces = spaces - 2
    
#loop iterates over the range from 0 to row + 1 , which corresponds to the number of hashes in the current row
    for space in range(0, row + 1):
        
#prints hash symbol and end = starts a new line
        print("# ", end="")
    print("")
