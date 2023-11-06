# class practice

class User:
    """class prints information about a user"""

    def __init__(self, first_name, last_name, member_since, username):
        self.first_name = first_name
        self.last_name = last_name
        self.member_since = member_since
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"User's Summary:\n{self.first_name} {self.last_name}\nMember since: {self.member_since}\nusername: {self.username}")

    def greet_user(self):
        print(f"\nWelcome back {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


user_1 = User("oscar", "perez", 2012, "oscarjvz100")
user_1.describe_user()
user_1.greet_user()
print(f"Logging Attempts: {user_1.increment_login_attempts()}")
