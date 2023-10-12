#program uses class composition to represent a video game

class VideoGame():
    '''Class to represent a video game'''
    def __init__(self, title, publisher, release, price):
        self.title = title
        self.publisher = publisher
        self.release = release
        self.price = price
        self.characters = Characters()
        self.weapons = WeaponsUsed()
        
    def game_info(self):
        info = f"{self.title} was made by {self.publisher} and released on "
        info += f"{self.release} with a price of {self.price}\n"
        print(info)

    
class Characters():
    '''class to represent characters in a video game/ for class composition'''
    def __init__(self):
        self.player = {
            'Leon S. kennedy:': 'Police officer', 
            'Ada Wong:': 'FBI agent?',
            'Marvin:': 'Lieutenant', 
            'Hunk:': 'Umbrella commander'
        }
        
    def characters_info(self):
        for name_key, profesion_value in self.player.items():
            print(f"-{name_key} {profesion_value}")


class WeaponsUsed():
    '''Class to represent weapons in a video game/ for class composition'''
    def __init__(self):
        self.weapons = [
                        'Matilda handgun', 'W870 shotgun', 'Hawk Magnum', 
                        'Flamethrower', 'Rocket Launcher']
    
    def weapons_play_1(self):
        for weapon in self.weapons:
            print(f"-{weapon}")


resident_evil = VideoGame(
    'Resident evil 2 Remake', 'Capcom', 'January 25, 2019', '$25.00'
)

print("\nGame #1 \n")
resident_evil.game_info()

print("-- Main Characters: --\n")
resident_evil.characters.characters_info()

print("\n-- Weapons Used by Leon S. kennedy --\n")
resident_evil.weapons.weapons_play_1()
