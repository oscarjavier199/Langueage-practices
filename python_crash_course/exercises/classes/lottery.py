from random import choice

lottery_options = [
    1, 4, 34, 26, 13, 11, 'A', 'R', 'Z', 'C', 'Q'
]

my_ticket = [1, 34, 4, 'R', 'C', 'Q']

print("\nAny ticket matching these 4 numbers or letters wins a prize!\n")

for number in range(1, 5):
        number = choice(lottery_options)
        print(f'-{number}')
if number == my_ticket:
    print("wou won")

