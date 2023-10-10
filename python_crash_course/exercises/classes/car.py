class Car:
    '''a class that represent a car'''
    
    def __init__(self, brand, model, year):
        
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def car_1(self):
        '''Return formatted descriptive info'''
        info_car_1 = f"{self.brand} {self.model} {self.year}"
        return info_car_1
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometers on it")
        
    def update_odometer(self, kilometers):
            self.odometer_reading = kilometers
            
    def increment_odometer(self, kilometers):
        '''add the given amount to the odometer reading'''
        self.odometer_reading += kilometers
        
class ElectricCar(Car):
    '''child class for electric car'''
    
    def __init__(self, brand, model, year):
        
        '''Initialize attributes of the parent class'''
        super().__init__(brand, model, year)
        self.battery_size = 40
        
    def battery(self):
        print(f"This car has a battery of {self.battery_size}.kWh\n")


electric_car_1 = ElectricCar('Tesla', 'model x', 2023)
print(electric_car_1.car_1())
electric_car_1.battery()
    
        
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.car_1())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(500)
my_used_car.read_odometer()
