requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry we ran out of green peppers')
    else:
        print(f'adding {requested_topping}')
        
print('-' * 20)

#checking if a list is empty:
requested_toppings_2 = []

if requested_toppings_2:
    for requested_topping_2 in requested_toppings_2:
        print(f"adding {requested_topping_2} to your pizza")
else:
    print(f"are you sure you want a plain pizza?")