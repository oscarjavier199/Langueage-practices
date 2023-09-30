#program will display a few examples of using multiple lists in
#for loops and we'll also use if statements to verify if
#an item in one list is also in the other list.

#first example using a pizzeria
available_toppings = ['pineapple', 'mushrooms', 'extra cheese',
'meat', 'chicken', 'olives', 'green peppers']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese', 
'meat', 'pasta']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to your pizza!")
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("Finished making your pizza!")

print("-" * 25)

#second example of multiple lists using car brands
car_brands = ['porsche', 'ferrari', 'maserati', 'bmw']
requested_cars = ['toyota', 'renault', 'porsche']

for requested_car in requested_cars:
    if requested_car in car_brands:
        print(f'we certainly have a few {requested_car} cars.')
    else:
        print(f'sorry, we don\'t have any {requested_car} cars at the moment')