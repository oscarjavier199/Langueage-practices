aliens = []

for alien in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10     

for alien in aliens[:6]:
    print(alien)
    print("...")
    
print(f"Total number of aliens: {len(aliens)}")