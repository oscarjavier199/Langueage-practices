# Make a class called Restaurant. The __init__() method for Restaurant
# should store two attributes: a restaurant_name and a cuisine_type.

from Restaurant_module import Restaurant
        
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
