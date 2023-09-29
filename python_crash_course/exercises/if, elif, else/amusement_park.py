age = 100

if age < 4:
    cost = 0
    
elif age < 18:
    cost = 25
    
elif age < 65:
    cost = 40
    
elif age >= 65:
    cost = 20
print(f'Your admission cost is ${cost}.')