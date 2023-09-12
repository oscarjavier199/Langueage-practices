#program will meow up to 3 times using a while loop.

""""
i = 1
while i <= 3:
    print("Meow")
    i += 1 #on each iteration i will increase until it is 3 and the program will stop.
"""

#this is other way of doing it, i will decrease until is 0 and the program will stop.
"""""
i = 3
while i != 0:
    print("Meow")
    i -= 1 #on each iteration i will decrease until it is 0 and the program will stop.#on each iteration i will decrease until it is 0 and the program will stop.
"""

#the same program can be written using less lines of code using a for loop
"""""
for i in [0,1,2]:
    print("Meow")
"""

#other way to do it without any loop is the following:    
"""""
print("Meow\n" * 3, end="")
"""

#we can also use the range function 
"""""
for i in range(3):
    print("Meow")
"""
    
#if we want to ask user for input:
"""""
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for i in range(n):
    print("meow")
"""

#if we want to create a function for the program:
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
    
def meow(n):
    for i in range(n):
        print("meow")
    
main()