class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.current_charge = 10
        
    def phone_info(self):
        print(f"\nYour phone ({self.brand} {self.model}) current charge is {self.current_charge}%\n")
        
    def charging(self):
        print('\nCharging...\n')
        
#! changing battery level (current_charge attribute) using a method:
    def new_battery_level(self, battery):
        self.current_charge = battery
        print(f"\nNew battery level: {self.current_charge}%")
        
#! updating battery level (not completly changing it, just updating it)

    def final_level(self, battery):
        self.current_charge += battery
        print(f"Final battery level: {self.current_charge}% ")



phone_1 = Phone('Iphone', '15 pro')
phone_1.phone_info()
phone_1.charging()
phone_1.new_battery_level(28)
phone_1.final_level(15)
