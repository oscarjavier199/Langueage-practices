from users_module import User, Admin, Privileges


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

        