class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = Engine()
        self.wheels = Wheels()
        self.energy = Energy()
        
    def car_info(self):
        print(f"\nCar: {self.brand} {self.model}\n")

class  Engine():
    def __init__(self):
        self.engine = [
            'v8 engine', '8700 RPM', 'Two electric motors', 
            'top speed: 345 km/h', 
        ]
    
    def engine_info(self):
        print(f"Engine Information: \n")
        for engine in self.engine:
            print(f"-{engine}")


class Wheels():
    def __init__(self, ):
        self.wheels_info = {
            'wheels:': ': 918 Spyder', 
            'material:': 'forged magnesium',
            'Front:': '9.5 J x 20',
            'Rear:': '12.5 J x 21 ',
        }
        
    def wheels_specs(self):
        print("\nWheels information: \n")
        for wheels_key, info_value in self.wheels_info.items():
            print(f"{wheels_key} {info_value}")


class Energy():
    def __init__(self):
        self.energy_supply = [
            'Lithium-ion battery', '6.8 KWh', '220 kW max power', 
            'compatible plug-in charger'
        ]
        
    def energy_specs(self):
        print("\nEnergy Information: \n")
        for energy in self.energy_supply:
            print(f"-{energy}")


porsche_spyder = Car('Porsche', '918 Spyder')
porsche_spyder.car_info()
porsche_spyder.engine.engine_info()
porsche_spyder.wheels.wheels_specs()
porsche_spyder.energy.energy_specs()