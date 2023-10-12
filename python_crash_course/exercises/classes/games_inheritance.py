class Games():
    def __init__(self, game_title, publisher, release_date, genre):
        self.game_title = game_title
        self.publisher = publisher
        self.release_date = release_date
        self.genre = genre
        
    def game_info(self):
        information = f"\n{self.game_title} was released by {self.publisher} on "
        information += f"{self.release_date} and it's a {self.genre} video game"
        print(information)
        
class Game2(Games):
    def __init__(self, game_title, publisher, release_date, genre, rating, reviews):
        super().__init__(game_title, publisher, release_date, genre)
        self.rating = rating
        self.reviews = reviews
        
    def game_info(self):
        information = f"\n{self.game_title} was released by {self.publisher} on "
        information += f"{self.release_date}, it's a {self.genre} video game, with a {self.rating} and most reviews are {self.reviews}"
        print(information)
        
class Game3(Games):
    def __init__(self, game_title, publisher, release_date, genre):
        super().__init__(game_title, publisher, release_date, genre)
        
    def game_info(self):
        information = f"\n{self.game_title} was released by {self.publisher} on "
        information += f"{self.release_date} and it's a {self.genre} video game"
        print(information)
        
        
        
game_1 = Games('Resident Evil 4', 'Capcom', '2023', 'Survival Horror')
game_1.game_info()

game_2 = Game2('Dead Space', 'Eletronic Arts', '2023', 'Horror', '18+ rating', '+ 4 stars')
game_2.game_info()

game_3 = Game3('Dead Island 2', 'Deep Silver', '2023', 'Horror')
game_3.game_info()

