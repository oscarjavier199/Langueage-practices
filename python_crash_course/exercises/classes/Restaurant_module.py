'''A class used to represent a restaurant information'''

class Restaurant():
    
    ''' Class to define a restaurant name and kind of food'''
    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.customers_served = 20

        
    def describe_restaurant(self):
        print(f"The restaurant is called {self.name} and they serve {self.cuisine}")
        
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