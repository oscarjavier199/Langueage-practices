# Make a class called Restaurant. The __init__() method for Restaurant
# should store two attributes: a restaurant_name and a cuisine_type.

class Restaurant():
    
    ''' Class to define a restaurant name and kind of food'''
    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.customers_served = 20

        
    def describe_restaurant(self):
        print(f"\nThe restaurant is called {self.name} and they serve {self.cuisine}")
        
    def open_restaurant(self):
        print(f"The restaurant is currently Open for business!")
        
    def close_restaurant(self):
        print(f"The restaurant is currently Closed for business, sorry")
        
    def open_time_restaurant(self):
        print(f"You shall pass!\n")
    
    def customers_today(self):
        print(f"Today we have served {self.customers_served} people!\n")

    def set_number_served(self, customers):
        self.customers_served = customers
        print(f"On monday morning they served {self.customers_served} people!")
        
    def increment_number_served(self, customers):
        self.customers_served += customers
        print(f"In the whole week they served {self.customers_served} people\n")
        
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
        
    def i_c_flavors(self):
        print("Available Ice creams:")
        for flavor in self.flavors:
            print(f"{flavor}")
                
                
IceCreamStand = IceCreamStand('Ice cream world', 'ice creams')
IceCreamStand.i_c_flavors()
    
    
restaurant_1 = Restaurant("Thai Tanic", "Thai food")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.customers_today()

restaurant_2 = Restaurant("Pickle Rick", "Vegan food")
restaurant_2.describe_restaurant()
restaurant_2.close_restaurant()
restaurant_2.set_number_served(67)
restaurant_2.increment_number_served(100)

restaurant_3 = Restaurant("Lord of the fries", "Fast food")
restaurant_3.describe_restaurant()
restaurant_3.open_time_restaurant()