number = input("Enter a number and I\'ll let you know if is even or odd >>> ")
number = int(number)

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")