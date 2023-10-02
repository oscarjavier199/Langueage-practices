#program show the simple use of .get() method in a dict, 
#if the key doesn't exists get() will print the given message, 
#if the key exists well get it's value

aliens_1 = {'color': 'green', 'speed': 'fast', 'points': 55}

points_value = aliens_1.get('points', 'No points assigned')

print(points_value)