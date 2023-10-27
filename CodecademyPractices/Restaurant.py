class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is open for business!")


restaurant = Restaurant("rick's lasagna", "Italian cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2_mex = Restaurant("mexictacos", "Mexican food")
restaurant_2_mex.describe_restaurant()
restaurant_2_mex.open_restaurant()

restaurant_3_fast_food = Restaurant("fasty", "Fast Food")
restaurant_3_fast_food.describe_restaurant()
restaurant_3_fast_food.open_restaurant()

