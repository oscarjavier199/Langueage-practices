#function definition and function call

def describe_city(city, country='germany'):
    print(f"\n{city.title()} is in {country.title()}")

describe_city('munich')
describe_city(city='oslo', country='norway')
describe_city(city='berlin')
describe_city('sydney', country='australia')