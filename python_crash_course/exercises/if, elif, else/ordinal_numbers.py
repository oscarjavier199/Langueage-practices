#program will print the proper ordinal ending for each number from 1 to 9

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if numbers:
    for number in numbers:
        if number == 1:
            print('1st')
        elif number == 2:
            print('2nd')
        elif number == 3:
            print('3rd')
        else:
            print(f"{number}th") 