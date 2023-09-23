
class Robot():
    def introduce_self(self): #we add self to every method we want to add to the class
        print("I'm a Robot and my name is " + self.name, "my color is " + self.color, "and my weight is:", + self.weight, "lbs")

#class atributes  
robot_1 = Robot()
robot_1.name = "Oscar"
robot_1.color = "Green"
robot_1.weight = 300

#class atributes 
robot_2 = Robot()
robot_2.name = "Alex"
robot_2.color = "Red"
robot_2.weight = 320

#class call
robot_1.introduce_self()
robot_2.introduce_self()

print("-" * 15)

#second exercise:

class Cat():
    def favourite_cat(self):
        print("My favourite cat is " + self.race, "they are kinda " + self.colour, "and they're from " + self.origin)

cat_1 = Cat()
cat_1.race = "phynx cat"
cat_1.colour = "greyish"
cat_1.origin = "Canada"

cat_1.favourite_cat()

print("-" * 15)


#third exercise

class Games():
    def video_games(self):
        print("One of my favourite games is " + self.name, "it is a " + self.genre, "the main character is " + self.character, "and it was released on " + self.release,
              "by " + self.publisher)
        print("." * 30 )

class Game_2():
    def video_games_2(self):
        print("But I also like " + self.game, "it is " + self.adventure, "the main character is " + self.human, "and it was released on " + self.date,
              "by " + self.published)
        print("." * 30 )

#class attributes for 1st class:
video_game_1 = Games()
video_game_1.name = "Resident Evil Village"
video_game_1.genre = "Survival Horror"
video_game_1.character = "Ethan Winters"
video_game_1.release = "2021"
video_game_1.publisher = "Capcom"

##class attributes for 2st class:
video_game_2 = Game_2()
video_game_2.game = "Assassin's Creed Valhalla"
video_game_2.adventure = "an adventure game"
video_game_2.human = "Eivor"
video_game_2.date = "2020"
video_game_2.published = "Ubisoft"

video_game_1.video_games()
video_game_2.video_games_2()


#same previous exercise but using constructors:

print("." * 30 )

class MyGame():
    def __init__(self, name, genre, character, date, publisher):
        self.name = name
        self.genre = genre
        self.character = character
        self.date = date
        self.publisher = publisher
        
    def new_game(self):
        print("My favourite video game is called " + self.name, "it is a " + self.genre, "kinda game, the main character is " + self.character,
              "it was released on " + self.date, "by " + self.publisher) 
        

game_1 = MyGame("Resident evil 4 remake", "Survival Horror", "Leon S. Keneddy", "2023", "Capcom")
game_2 = MyGame("Bloodborne", "Horror maybe?", "'The Hunter'", "2015", "Sony")

game_1.new_game()
game_2.new_game()


print("." * 30 )

# new exercise using constructor:

class Cars():
    def __init__(self, brand, colour, country, type):
        self.brand = brand
        self.colour = colour
        self.country = country
        self.type = type
    def fav_car(self):
        print("My favourite Car brand is " + self.brand, "I love the " + self.colour, "colour, " + self.brand, "is from " + self.country, "and is a " + self.type)

car_1 = Cars("Porsche", "Black", "Germany", "sports car")
car_2 = Cars("Ferrari", "Red", "Italy", "Convertible car")

car_1.fav_car()
car_2.fav_car()



