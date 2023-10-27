class User:
    def __init__(self, first_name, last_name, member_since, username):
        self.first_name = first_name
        self.last_name = last_name
        self.member_since = member_since
        self.username = username

    def describe_user(self):
        print(
            f"User's Summary:\n{self.first_name} {self.last_name}\nMember since: {self.member_since}\nusername: {self.username}")

    def greet_user(self):
        print(f"\nWelcome back {self.username}!")


user_1 = User("oscar", "perez", 2012, "oscarjvz100")
user_1.describe_user()
user_1.greet_user()
