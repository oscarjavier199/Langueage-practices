def city_country(city, country, population=''):
    
    '''returns a city and its country formatted'''
    
    if population:
        city_and_country = f"{city}, {country} - {population}"
    else:
        city_and_country = f"{city}, {country}"
        
    return city_and_country.title()

city_country('Santiago', 'Chile', population='population = 5000000')
