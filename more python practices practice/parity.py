#program takes a number as input and determines if it is an even or odd number

#main function
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even Number")
    else:
        print("Odd Number")

#reusable funtion
def is_even(n): #defining function, (n) represents number
    if n % 2 == 0:
        return n % 2 == 0 #we can also write it as (return True if n % 2 == 0 else False)

main() #calling main function