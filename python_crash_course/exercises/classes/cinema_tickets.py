class tickets():
    
    def __init__(self, movie):
        self.movie = movie
        self.tickets = 20
        
    def available_tickets(self):
        print(f"\nWe have {self.tickets} tickets for {self.movie}")
        print("...\n")
        
    def sold_tickets(self, tickets_left):
        self.tickets = tickets_left
        print(f"Attention! we only have {self.tickets} tickets left, please hurry and buy yours\n")
        
    def last_chance(self, tickets_left):
        self.tickets -= tickets_left
        print(f"Warned you, now we only have {self.tickets} ticket... and it's MINE!\n")

class MoreTickets(tickets):
    def __init__(self, movie):
        super().__init__(movie)
        self.new_movie = NewMovie()
        
    def new_chance(self):
        print(f"\nAlright! I changed my mind\n")
        self.tickets = 100
        print(f"Now we have {self.tickets} tickets!!!")
    
class NewMovie:
    def __init__(self):
        self.movies = [
            'Dune', 'mission impossible', 'The Batman'
            ] 
        
    def movies_list(self):
        for movie in self.movies:
            print(f"--{movie}")
        
    

movie_1 = tickets('The Lord of the Flies')
movie_1.available_tickets()
movie_1.sold_tickets(5)
movie_1.last_chance(4)

new_tickets = MoreTickets('movies')
new_tickets.new_chance()
print(f"\n\tWe also have some new Movies: ")
new_tickets.new_movie.movies_list()
