available_cars = {
    'porsche': '2024',
    'mazda': '2023',
    'bmw': '2024', 
    'volkswagen': '2023',
    'maserati': '2024',
}

print(f"we have the following cars:")

new_cars = ['porsche', 'bmw', 'maserati']

for key in available_cars.keys():
    print(key)
    if key in new_cars:
        value = available_cars[key].title()
        print(f"\tmodel {value}")