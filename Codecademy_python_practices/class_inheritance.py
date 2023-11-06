class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My ID is {self.id}")


class User:
    def __init__(self, username, role='Customer'):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"My username is {self.username}")
        print(f"My role is {self.role}")


# Admin class inherits from two classes
class Admin(Employee, User):

    # Using super to invoke parent's method
    def __init__(self):
        super().__init__()
        # invoke or call the .__init__() method od User class
        User.__init__(self, self.id, 'Admin')


# Multiple inheritance
class Manager(Admin):

    def say_id(self):
        super().say_id()
        print("We are in charge around here!")


e1 = Employee()
e1.say_id()

e2 = Employee()
e2.say_id()

e3 = Admin()
e3.say_user_info()

print("*" * 30)

# multiple inheritance example
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def action(self):
        print("{} wags tail. Awwww".format(self.name))


class Wolf(Animal):
    def action(self):
        print("{} bites. OUCH!".format(self.name))


class Hybrid(Dog, Wolf):
    def action(self):
        Dog.action(self)
        Wolf.action(self)


my_pet = Hybrid("Fluffy")
my_pet.action()
