def greet_someone():
# This program will take input from the user and then
# show the output.
# The program was designed to test the input and output codes
    name = input ('whats your name?')
    hometown = input('And where are you from?')
    print('Very nice to meet you, {}!'.format(name), f'from {hometown}!')
greet_someone()