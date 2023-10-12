class Movies():
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
        
    def movie_info(self):
        print(f"\n- The movie is {self.title}, directed by {self.director}, it was released on {self.year}")


class Movie2(Movies):
    def __init__(self, title, director, year, rating):
        super().__init__(title, director, year)
        self.rating = rating
        
    def movie_info(self):
        print(f"\n- The movie is {self.title}, directed by {self.director}, it was released on {self.year} with a {self.rating} rating")


class Movie3(Movies):
    def __init__(self, title, director, year, reviews):
        super().__init__(title, director, year)
        self.reviews = reviews
        
    def movie_info(self):
        print(f"\n- The movie is {self.title}, directed by {self.director}, it was released on {self.year} with {self.reviews}.")
        
 
movie_1 = Movies('Lord of the rings', 'peter jackson', 2000)
movie_1.movie_info()

movie_2 = Movie2('Harry Potter', 'Michael Bay', 2001, rating='pg 13')
movie_2.movie_info()

movie_3 = Movie3('Hellboy', 'Gillermo Del Toro', 2006, 'Mixed reviews')
movie_3.movie_info()