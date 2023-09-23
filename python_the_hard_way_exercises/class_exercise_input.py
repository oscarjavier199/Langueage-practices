class Tv():
    def __init__(self, name):
        self.name = name
        
    def tv_series(self):
        print("Whats your favorite TV series? ")
        print("options: " + self.name)
        user_input = input("> ")
        if user_input == "1":
            print("Great choice, The simposons is really funny")
        elif user_input == "2":
            print("I love it too! Rick always makes me laugh and Jerry is just hilarious")
        elif user_input == "3":
            print("Hello Brother...")
            print("Did you get it?")
            print("That's what Damon always says to... forget it")
        else:
            print("Never herd of that one... will watch it later though")
            
fave_tv = Tv("1. The Simpsons " "2.Rick and Morty " "3.The Vampire Diaries ")

fave_tv.tv_series()

# 
class Food():
    def __int__(self, dish, restaurant, restaurant_2, restaurant_3, restaurant_4):
        self.dish = dish
        self.restaurant = restaurant
        self.restaurant_2 = restaurant_2
        self.restaurant_3 = restaurant_3
        self.restaurant_4 = restaurant_4
        
    def fave_food(self):
        print("What's your favorite Food? ")
        print("...")
        print(f"options: {self.dish}")
        user_input = input.lower("> ")
        if user_input == "pizza":
            print("Who doesn't love pizza right?")
        elif user_input == "asagna":
            print("Love it!")
        elif user_input == "brownies":
            print("There is nothing I love more than a brownie with milk")
        elif user_input == "None":
            print("Well, who needs that kind f food right?")
        else:
            print("Never eaten that, will try it later!")
            
        
        
meals = Food("Pizza - Burger - Lasagna - Brownies - None", "Papa jhons", "Stouffer's", "MCdonalds", "donkin' donuts", "get out of here...")
meals.fave_food()