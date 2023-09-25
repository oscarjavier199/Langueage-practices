rows  = 10
for row in range(rows + 1,  0,  -1):
    for space in range(0, row - 1):
        print("# ", end=" ")
    print("")
    
'''
The first line sets a variable called rows to the value of 10. 
This means that the triangle will have 10 rows of hash symbols.


The second line starts a for loop that iterates over a range of 
numbers from rows + 1 (which is 11) to 0, with a step of -1. This means that 
the loop will run 11 times, with the variable row decreasing by 1 each time. 
For example, on the first iteration, row will be 11, on the second iteration, 
row will be 10, and so on, until row reaches 0.


The third line starts another for loop inside the first loop that iterates over a 
range of numbers from 0 to row - 1. This means that the inner loop will run row - 1 
times, with the variable space increasing by 1 each time. For example, on the first 
iteration of the outer loop, when row is 11, the inner loop will run 10 times, with space 
going from 0 to 9. On the second iteration of the outer loop, when row is 10, the inner loop 
will run 9 times, with space going from 0 to 8, and so on.

The fourth line prints a hash symbol (#) followed by a space, using the end parameter to 
prevent a new line from being printed. This line will be executed space times, which means 
that the number of hash symbols printed on each row will decrease by 1 as row decreases.
For example, on the first row, 10 hash symbols will be printed, on the second row, 9 hash symbols 
will be printed, and so on, until the last row, where only 1 hash symbol will be printed.


The fifth line prints an empty string, which causes a new line to be printed. 
This line will be executed once for each iteration of the outer loop, which means that a new 
line will be added after each row of hash symbols.
'''