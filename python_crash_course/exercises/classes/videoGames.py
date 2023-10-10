class Games():
    def __init__(self):
        self.new_games = [
            'Resident evil 4 remake', 'Hogwarts Legacy', 
            'Dead island 2', 'dead space remake'
        ]
    
    def iterate_games(self):
        for game in self.new_games:
            print(f"--{game}\n")
            

class coming_games():
    def __init__(self):
        self.future_games = [
            'Avatar', 'Silent Hill 2', 'Lies of P', 'separate ways',
            'MK 1', 'assassin\'s creed mirage', 'The Lords of the Fallen'
        ]
    
    def next_games(self):
        for future_game in self.future_games:
            print(f"--{future_game}")
        
                
games_list = Games()
print(f"\n\tThis year's released video games: \n")
games_list.iterate_games()

print(f"\n\tComing later this year: \n")
not_released = coming_games()
not_released.next_games()