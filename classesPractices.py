class Dog:
    def __int__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def roll_over(self):
        print(f"{self.name} is rolling over!")

dog_1 = Dog('Scooby', 12, 'brown')
dog_1.roll_over()