favorite_places = {
    'alex': ['central park', 'cinema', 'shopping mall'],
    'mike': ['home', 'cinema', 'park', 'norway'],
    'elena': ['italy', 'france', 'eiffel tower'],
    'caroline': ['museum', 'stadium', "grandma\'s house"],
}

print("\nMy friends and Their favorite places are: \n")
for friends_1, places in favorite_places.items():
    print(f"{friends_1}: {places}")