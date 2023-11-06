# **kwarg practice

def car_info(brand, model, **additional_info):
    """function takes **kwargs to print information about a car"""

    additional_info['Brand'] = brand
    additional_info['Model'] = model
    return additional_info


car = car_info('porsche', 'spyder', color='red', tow_package=True, engine='V8')
print(car)
