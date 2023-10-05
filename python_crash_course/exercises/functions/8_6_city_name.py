#function definition with 2 parameters
#function call will print a message in format "city, country"

def city_country(city, country):
    
    c_c_info = f"{city}, {country}"
    return c_c_info.title()

message = city_country('oslo', 'norway')
print(f'{message}')

message = city_country('munich', 'germany')
print(f"{message}")

message = city_country('copenaghen', 'denmark')
print(message)