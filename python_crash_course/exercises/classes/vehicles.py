class Vehicles():
    def __init__(self, v_type, model, speed):
        self.v_type = v_type
        self.model = model
        self.speed = speed
        self.engine = 'Pratt & Whitney F100'

        
    def vehicle_description(self):
        vehicle_1 = f"\nThis {self.model} {self.v_type} can go as fast "
        vehicle_1 += f"as {self.speed} kp/h! with a powerful {self.engine} engine\n"
        print(vehicle_1)
        
        
class Car(Vehicles):
    def __init__(self, v_type, model, speed, color):
        super().__init__(v_type, model, speed)
        self.color = color
        self.engine = 'V8'
        
    def vehicle_description(self):
        vehicle_2 = f"This {self.v_type} {self.model} comes in {self.color} and its "
        vehicle_2 += f"speed is {self.speed} kp/h, engine ({self.engine})!"
        print(vehicle_2)


class ElectricCar(Vehicles):
    def __init__(self, v_type, model, speed, color):
        super().__init__(v_type, model, speed)
        self.color = color
        self.engine = 'None'
        self.fuel = 'Electric Vehicle'
        
    def vehicle_description(self):
        electric_car = f"\nThe {self.v_type} {self.model}, comes in a {self.color}"
        electric_car += f", it's engine?\n{self.engine}. \nWhy?\nBecause its an {self.fuel}."
        print(f"{electric_car}\nSpeed?\n{self.speed} kp/h!")


class Bicycle(Vehicles):
    def __init__(self, v_type, model, speed):
        super().__init__(v_type, model, speed)
        self.characteristics = {
            'Type': 'Bicycle', 
            'speed': 'Depends on user',
            'color': 'Red/white',
            'Engine': 'Not applicable',
        }
    
    def vehicle_description(self):
        for characteristic_key, vehicle_value in self.characteristics.items():
            print(f"{characteristic_key, vehicle_value}")


class Boat(Vehicles):
    def __init__(self, v_type, model, speed):
        super().__init__(v_type, model, speed)
        
    def vehicle_description(self):
        print(f"The {self.v_type} '{self.model}' its max speed is {self.speed}\n")


print("-" * 30)
airplane = Vehicles(model='F-16', v_type='Fighting plane', speed=2100)
airplane.vehicle_description()
print("-" * 30)

car = Car(v_type='Porsche', model='Spyder', speed=345, color='Sky-Blue')
car.vehicle_description()
print("-" * 30)

electric_vehicle = ElectricCar(v_type='Tesla', model='model Y', speed=217, color='custom color')
electric_vehicle.vehicle_description()
print("-" * 30)

no_engine_vehicle = Bicycle('bicycle', 'road bike', 'depends on user')
print("\nVehicle:\n") 
no_engine_vehicle.vehicle_description()
print("-" * 30)

print(f"\nWe have the following boats for you: \n")
available_boats = Boat('Cruise ship', 'Icon of the Seas', '41 km/h')
available_boats.vehicle_description()
available_boats_2 = Boat('Electric Boat', 'Tûranor PlanetSolar', '19 km/h')
available_boats_2.vehicle_description()
print("-" * 30)
