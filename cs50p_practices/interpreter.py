#program will ask user for an arithmetic expression such as 1 + 1 
#and return the result in a floating number, like 2.0.

def main():
    expression()
    
def expression():
    
    num1, user_expression, num2 = input("Expression please: ").split(" ") #num1 represents the first number entered by user, num2 represents the second one
    #user_expression represents the arithmetic operation (+, -, *, /),  split will get rid of the spaces entered by user.
    
    num1 = float(num1) #converts int to floats
    num2 = float(num2)
    
    if user_expression == "+": 
        print(f"Answer: {num1 + num2:.1f}") #:.1f is to format the answer to only get one digit after the decimal point
    elif "-":
        print(f"Answer: {num1 - num2:.1f}")
    elif "*":
        print(f"Answer: {num1 * num2:.1f}")
    elif "/":
        print(f"Answer: {num1 / num2:.1f}")
    else:
        print("0.0")
    
if __name__ == "__main__":
    main()
