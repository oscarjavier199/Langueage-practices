#adding function
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

#subtracting function
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

#multiplying function
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

#dividing function
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

#print
print("Let's do some math with just functions!")

#here we are calling the functions previously defined and assigning them to some variables
age= add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(200, 2)

#print message "Age: 35, Height: 74, weight: 180, IQ: 50"
print("Age: %d, Height: %d, weight: %d, IQ: %d" % (age, height, weight, iq))

#print message "Here is a puzzle:"
print("Here is a puzzle:")

#divides the iq by 2 then multiplies it by the weight, subtracts tge height and adds the age.
# we are taking the return values of the functions and using them as the arguments of another function
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#prints message
print("That becomes: ", what, "\nCan you do it by hand?")
