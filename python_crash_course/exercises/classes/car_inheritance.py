class Car():
    '''A class that represents a car'''
    def __init__(self, brand, model, color, engine):
        self.brand = brand
        self.model =  model
        self.color = color
        self.engine = engine
        
    def car_specs(self):
        car_info = f"\nThe {self.brand} {self.model} comes in {self.color} with a"
        car_info += f" powerful {self.engine} engine!"
        print(car_info)

class ElectricCar(Car):
    '''a child class that represents an electric car'''
    def __init__(self, brand, model, color, engine, battery, price):
        super().__init__(brand, model, color, engine)
        self.battery = battery
        self.price = price
        
    def car_specs(self):
        car_info = f"\nThe {self.brand} {self.model} comes in {self.color}, with ..."
        car_info += f"{self.engine}! because its electric! Its battery has a "
        car_info += f"capacity of {self.battery} and the price... {self.price}\n"
        print(car_info)

class Sport(Car):
    '''A class to represent a sports car'''
    def __init__(
        self, brand, model, color, engine, power, passengers, doors, top_speed
    ):
        super().__init__(brand, model, color, engine)
        self.power = power
        self.passengers = passengers
        self.doors = doors
        self.top_speed = top_speed
        
    def car_specs(self):
        car_info = f"The {self.brand} {self.model} comes in {self.color}, with a "
        car_info += f"{self.engine} engine! {self.power} power! space for {self.passengers}"
        car_info += f" and {self.doors} doors, and a killer {self.top_speed} Top Speed.\n"
        print(car_info)


car_1 = Car('BMW', 'X5', 'mate black', 'V8')
car_1.car_specs()

electric_car = ElectricCar(
    'Chevrolet' ,'Bolt 2023', 'yellow', 'No Engine', battery='200 kwh', 
    price='$ 26.000'
)
electric_car.car_specs()

sports_car = Sport(
    'Bugatti', 'Chiron super sport 300+', 'orange and black', 'Quad-turbo W16', 
    '1600 hp', 2, 2, '305 mph'
)
sports_car.car_specs()
