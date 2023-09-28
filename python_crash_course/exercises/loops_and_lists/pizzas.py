pizzas = ['hawaiian', 'pepperoni', 'mushroom chicken']
print('pizzas:')

for pizza in pizzas:
    print(f'I really like {pizza} pizza')
    
    
friend_pizzas = pizzas[:]
pizzas.append('fruits')
friend_pizzas.append('meat')

print('My favorite pizzas are')
for pizza in pizzas:
    print(f'** {pizza}')
    
print('\nMy friends favorite pizzas are:')
for friend_pizza in friend_pizzas:
    print(f'** {friend_pizza}')
