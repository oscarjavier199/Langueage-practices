favorite_languages = {
    'jen': 'python', 
    'edward': 'c',
    'mike': 'ruby', 
    'alex': 'c++',
}

friends = ['mike', 'alex']

for name in favorite_languages.keys():
    print(f"Hi {name}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name} I see you love {language}")

if 'Erin' != favorite_languages:
    print("Erin please take our poll!")
    