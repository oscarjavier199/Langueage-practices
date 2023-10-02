rivers = {'nile': 'egypt',
          'Thames': 'England',
          'amazon river': 'Colombia and Brasil',
          'Yangtze River': 'China',
          'The Ob': 'Russia',
}

for river_name, location in rivers.items():
    print(f"the {river_name.title()} is located in {location.title()}")

print("\nRivers in Dictionary:")

for river_key in rivers.keys():
    print(f"{river_key.title()}")

print("\nCountries in Dictionary:")
for countries in rivers.values():
    print(f"{countries.title()}")