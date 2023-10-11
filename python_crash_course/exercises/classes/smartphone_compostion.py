class SmartPhone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.screen_size = 6.7
        self.storage = 256
        self.battery = Battery()
        self.cameras = Cameras()
        self.software = Software()
        
    def phone_info(self):
        info = f"\nThe {self.brand} {self.model} has a {self.screen_size} inch screen"
        info += f" and {self.storage} GB of storage.\n"
        print(info)


class Battery():
    def __init__(self):
        self.brand = 'Samsung'
        self.capacity = 5000
        self.model = 'SMNG23'
        self.origin = 'China'
        
    def battery_specs(self):
        battery_info = f"Battery: {self.brand} model {self.model}, capacity of "
        battery_info += f"{self.capacity} mAh and it was made in {self.origin}\n"
        print(battery_info)


class Cameras():
    def __init__(self):
        self.brand = 'Sony'
        self.pixels = 50
        self.resolution ='4K'
        self.origin = 'Japan'
        
    def cameras_specs(self):
        camera_info = f"Camera: {self.brand} dual camera, {self.pixels} "
        camera_info += f"pixels each with a {self.resolution} resolution, they were made in {self.origin}.\n"
        print(camera_info)


class Software():
    def __init__(self):
        self.os = 'Android'
        self.os_version = 15
        self.processor = 'SnapDragon'
        self.sim = 'Dual'
        self.network = '5g'
        self.ui = 'Samsung One'
        
    def software_info(self):
        print(f"""Software: This phone's operating system is {self.os} {self.os_version}
and a {self.ui} UI, the processor is a {self.processor}, 
{self.sim} Sim and {self.network} connectivity.\n""")


smart_phone_1 = SmartPhone('Samsung', 'S23 ultra')
smart_phone_1.phone_info()

smart_phone_1.battery.battery_specs()
smart_phone_1.cameras.cameras_specs()
smart_phone_1.software.software_info()
