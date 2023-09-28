#program will use for loops, list slicing, append() and pop()
# to print a message

my_movies = ['harry potter', 'the lord of the rings', 'sicario', 'narnia']
friends_movies = my_movies[:]

print('\nmy favorite movies are:')
for my_movie in my_movies: print('*', my_movie.title())


friends_movies.append('scary movie')
friends_movies.pop(0)
friends_movies.pop(3)


print('\nMy friend\'s favorite movies are:')
for friend_movie in friends_movies: print('*', friend_movie)
    