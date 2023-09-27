#combining strings:

first_name = 'ada'
last_name  = 'lovelace'
full_name =  f'{first_name} {last_name}'
print(full_name)
print('-' * 10)

#we can assign a f-string to a variable
message = f'Hello {full_name.title()}'
#and then we can print that variable.
print(message)