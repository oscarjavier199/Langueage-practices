#simple program to show the functionality of dictionaries with multiple keys

favorite_language = {
    'jen': 'python', 
    'mike': 'C', 
    'oscar': 'python',
    'edward': 'python'
}

#assign the key we want to print to a new variable, so print() looks cleaner
languages = favorite_language['edward'].title()
print(f"Edward's favorite language is {languages}")

languages_2 = favorite_language['oscar'].title()
print(f"oscar's favorite language is {languages_2}")
