from city_functions import city_country

def test_city_country():
    '''Tests city and country'''
    city_and_country = city_country('Santiago', 'Chile')
    assert city_and_country == 'Santiago, Chile'


def test_population():
    '''Tests a third parameter (population)'''
    population = city_country('Santiago', 'Chile', 'population = 5000000')
    assert population == 'Santiago, Chile - Population = 5000000'