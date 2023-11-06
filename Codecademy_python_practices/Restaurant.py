# program shows the use of class inheritance

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is open for business!\n")

    def num_customers(self, number_served):
        return self.number_served + number_served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla', 'chocolate', 'cookies and cream', 'brownie']

    def open_restaurant(self):
        print("Restaurant will be open for business after 4:00 pm!")

    def ice_flavors(self):
        print("Ice Cream Flavors: ")
        for flavor in self.flavors:
            print(f"-{flavor}")


restaurant = Restaurant("rick's lasagna", "Italian cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"Customers served: {restaurant.num_customers(45)}\n")

restaurant_2_mex = Restaurant("mexictacos", "Mexican food")
restaurant_2_mex.describe_restaurant()
restaurant_2_mex.open_restaurant()

restaurant_3_fast_food = Restaurant("fasty", "Fast Food")
restaurant_3_fast_food.describe_restaurant()
restaurant_3_fast_food.open_restaurant()

ice_cream_shop = IceCreamStand("Cookies & cream", "Ice creams and desserts")
ice_cream_shop.describe_restaurant()
ice_cream_shop.open_restaurant()
ice_cream_shop.ice_flavors()
