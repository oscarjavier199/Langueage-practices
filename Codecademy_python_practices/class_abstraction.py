from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


class Porsche(Car):
    def mileage(self):
        print("The Porsche 911 is 331 Kmph")


class Tesla(Car):
    def mileage(self):
        print("The Tesla Model x is 200 Kmph")


class Ferrari(Car):
    def mileage(self):
        print("The Ferrari f40 is 201 Kmph")


por = Porsche()
por.mileage()

fer = Ferrari()
fer.mileage()

tes = Tesla()
tes.mileage()

print("*" * 30)

# Second Example

class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass


# Write your code below
class Employee(AbstractEmployee):
    def say_id(self):
        print("I am the boss!")


e1 = Employee()
e1.say_id()
