class Update_pc():
    '''practices on updating attributes / not for use'''
    
    def __init__(self, pc_brand):
        self.pc_brand = pc_brand
        self.version = 13
        
    def current_version(self):
        message = f"\nYour pc is an ({self.pc_brand}) "
        message += f"and its current version is: {self.version}\n"
        print(f"{message}")
        
    def new_version_available(self):
        print(f"... new version available!\nPlease Update")
        
    def new_version_update(self):
        print(f"\ncongrats! updated to version {self.version}")
        
    
        
        
computer_1 = Update_pc('Asus')
computer_1.current_version()
computer_1.new_version_available()

#! updating battery level directly
computer_1.version = 15
computer_1.new_version_update()


