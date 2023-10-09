class Dog:
    ''' an attempt to model a dog'''
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
#!sit is a method of class Dog
    def sit(self): 
        print(f"{self.name} is sitting!")

#!roll_over is a method of class Dog
    def roll_over(self): 
        print(f"{self.name} is rolling over!")

#!my_dog and your_dog is an instance of class Dog
my_dog = Dog('Gandalf', 5)
your_dog = Dog('Galadriel', 3)

print(f"\nMy dog's name is {my_dog.name}")
print(f"{my_dog.name}'s {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"{your_dog.name}'s {your_dog.age} years old\n")
your_dog.roll_over()


