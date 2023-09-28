my_foods = ['pizza', 'hamburger', 'cereal']
friend_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('steak')
friend_foods.append('ice cream')

print('\nupdated list:')
print(my_foods)
print('\nfriend\'s updated list')
print(friend_foods)