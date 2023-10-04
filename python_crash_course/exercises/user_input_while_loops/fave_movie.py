movie_flag = True

prompt += ("\nEnter 'quit' to end the program >>> ")


while movie_flag:
    fave_movie = input(prompt)
    if fave_movie == 'quit':
        movie_flag = False
    else:
        print('That\'s my favorite movie too! ')
        movie_flag = False
    