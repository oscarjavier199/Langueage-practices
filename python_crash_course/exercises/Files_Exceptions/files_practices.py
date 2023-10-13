print("Enter two numbers and I'll multiply them ")
print("Enter 'q' to quit")

while True:
    num_1 = input("Number 1: ")
    if num_1 == 'q':
        break
    
    num_2 = input("Number 2: ")
    if num_2 == 'q':
        break
    
    try:
        answer = int(num_1) * int(num_2)
    except ValueError:
        print("Please enter numeric values only")
    else:
        print(answer)