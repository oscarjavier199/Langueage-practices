#Write a function that stores information about a car in a dictionary.

def cars(brand, model, **specs):
    specs['Brand'] = brand
    specs['Model'] = model
    return specs

make_Car = cars('porsche', 'spyder',
                color='Blue', 
                tow_package='False'
                )

print(f"Car = {make_Car}")