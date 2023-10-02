#program will print some words and their meaning using a dictionary

glossary = {
    'python': 'programming language',
    'dictionary': 'connects pieces of related data',
    'lists': 'stores multiple items in a single variable',
    'int': 'integer number (1)',
    'float': 'floating number (1.0)',
    'C': 'general-purpose programming language',
    'key-value': 'database types',
    'IDLE': 'integrated development environment for Python',
    'SQL': 'Structured Query Language',
    'Django': 'Python-based web framework',
}

for term, meaning in glossary.items():
    print(f"{term}:\n{meaning}\n")
