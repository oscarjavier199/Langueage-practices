def cars_info(car, origin='germany'):
    new_cars = f"{car.title()} is from {origin.title()}"
    return new_cars

info = cars_info('porsche')
print(info)

info = cars_info('tesla', origin='USA')
print(info)

info = cars_info('maserati', origin='italy')
print(info)

info = cars_info('Volvo', origin='sweden')
print(info)