def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)


hex_output()


def hex_output():
    number_to_hex = input("\nplease enter number to convert to hex: >>> \n")

    try:
        while True:
            int_num = int(number_to_hex)
            print(f"Hexadecimal: {hex(int_num)}\n")
            break
    except ValueError:
        print("Sorry, only numbers are accepted, try again")


hex_output()

