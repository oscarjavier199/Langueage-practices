class User():
    
    '''Class defines information of some users (user_name, last logging and
    device used)'''
    
    def __init__(self, user_name, logged_in, device):
        self.user_name = user_name
        self.logged_in = logged_in
        self.device = device
        self.logging_attempts = 0
        
    def describe_user(self):
        print(f"\nuser: {self.user_name} last logged in {self.logged_in}, using a {self.device}")
    
    def greet_user(self):
        print(f"Welcome back {self.user_name}, nice to have you back!\n")
        
    def increment_login_attempts(self):
        self.logging_attempts += 1
        print(f"Logging attempts: {self.logging_attempts}")
        
    def reset_logging_attempts(self):
            self.logging_attempts = 0 
            print(f"New attempts: {self.logging_attempts}")
            
class Admin(User):
    def __init__(self, user_name, logged_in, device):
        super().__init__(user_name, logged_in, device)
        self.privileges = Privileges()
        
            
class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post", "can delete post", "can ban user", 
            "can delete accounts", "can suspend accounts"
        ]
    
    def show_privileges(self):  
        print(f"\nAdmin privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")
        

Admin_1 = Admin('Admin', 'Hidden', 'Hidden')
Admin_1.privileges.show_privileges()

user_1 = User("jack_sparrow1", "01/02/2000", "nokia")
user_1.describe_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_logging_attempts()
user_1.greet_user()



user_2 = User('pickle_RICK', '12/23/22', "samsung phone")
user_2.describe_user()
user_2.greet_user()

user_3 = User("BatMan06", "02/04/2018", "computer")
user_3.describe_user()
user_3.greet_user()

        