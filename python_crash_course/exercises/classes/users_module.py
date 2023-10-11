
from users_module_2 import User

class Admin(User):
    def __init__(self, user_name, logged_in, device):
        super().__init__(user_name, logged_in, device)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = [
            "can add post", "can delete post", "can ban user", 
            "can delete accounts", "can suspend accounts"
        ]
    
    def show_privileges(self):  
        print(f"\nAdmin privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")
