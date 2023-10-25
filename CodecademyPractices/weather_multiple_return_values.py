weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']


def weather_report(weather):
    """Multiple return values"""

    first_day = f" Tomorrow the weather will be {weather[0]}"
    second_day = f" Tomorrow the weather will be {weather[1]}"
    third_day = f" Tomorrow the weather will be {weather[2]}"
    return first_day, second_day, third_day


monday, tuesday, wednesday = weather_report(weather_data)

print(monday)
print(tuesday)
print(wednesday)
