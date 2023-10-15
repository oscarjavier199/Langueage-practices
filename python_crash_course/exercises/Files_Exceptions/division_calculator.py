
print("Give me two numbers and I'll divide them ")
print("Enter 'q' to quit")

try:
    while True:
        number_1 = input("Number 1: ")
        if number_1 == 'q':
            break
        number_2 = input("Number 2: ")
        if number_2 == 'q':
            break
        answer = int(number_1) / int(number_2)
        print(answer)

except ZeroDivisionError:
    print("you can't divide by zero!")
except ValueError:
    print("Please enter a number")
