#program takes a number as input and determines if it is an even or odd number

#main function
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even Number")
    else:
        print("Odd Number")

#reusable funtion to determine if input given is true or false
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()