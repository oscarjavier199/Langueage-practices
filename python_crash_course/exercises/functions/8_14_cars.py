#Write a function that stores information about a car in a dictionary.

def cars(brand, model, **specs):
    
    '''adds two key-value pairs to a dictionary created as parameter
    and receives as many key-value pairs as needed'''
    
    specs['Brand'] = brand
    specs['Model'] = model
    return specs

make_Car = cars('porsche', 'spyder',
                color='Blue', 
                tow_package='False'
                )

print(f"Car = {make_Car}")