heroes_glossary = {
    'batman': 'bruce wayne',
    'iron man': 'tony stark',
    'hulk': 'bruce banner',
    'superman': 'clark kent',
    'spiderman': 'peter parker',
    'constantine': 'jhon constantine',
}

villains_glossary = {
    'joker': 'jack oswald white',
    'M.O.D.O.K': 'george tarleton',
    'ABOMINATION': 'emil blonsky',
    'Darkside': 'UXAS',
    'venom': 'eddie brock',
    'the great darkness': 'soul of darkness itself',
}

heroes_and_villains = [heroes_glossary, villains_glossary]

print("\nGlossary of heroes / villains and their real names:\n")
for heroes_villains in heroes_and_villains:
    print(f"Glosary: {heroes_villains}\n")