class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My ID is {self.id}")


class Admin(Employee):
    def say_id(self):
        print("I am an admin!")


e1 = Employee()
e1.say_id()

e2 = Employee()
e2.say_id()

e3 = Admin()
e3.say_id()
