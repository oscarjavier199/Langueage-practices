#program will access the values of some keys

favorite_numbers = {
    'charlie': [2, 3, 4, 5],
    'michael': [55, 9, 13],
    'yolanda': [777, 6, 3], 
    'rick': [1, 2, 3, 14], 
    'walter': [3, 14, 16, 25],
}

for person, number in favorite_numbers.items():
    print(f"\n\t{person}'s favorite numbers are: {number} 🙃")
