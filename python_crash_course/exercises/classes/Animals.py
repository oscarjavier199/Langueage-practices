class Animal():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def make_sound(self):
        print(f"\nThe {self.name} makes {self.sound}\n")


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed
        
    '''override the parent class attribute make_sound'''
    def make_sound(self):
        print(f"{self.name} is a {self.breed} and makes {self.sound}\n")


class Cat(Animal):
    def __init__(self, name, sound, color, animal):
        super().__init__(name, sound)
        self.color = color
        self.animal = animal
    
    '''override parent class method'''
    def make_sound(self):
        print(f"{self.name} is a {self.color} {self.animal} and makes {self.sound}\n")


class Bird(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
        self.can_fly = False
    
    '''override parent class method'''
    def make_sound(self):
        if self.can_fly == True:
            print(f"{self.name} says {self.sound} and can fly")
        else:
            cannot_fly = f"{self.name} says {self.sound} and... OMG {self.name}"
            cannot_fly += f" had an accident, {self.name} cannot fly"
            print(cannot_fly)

    
class Fish(Animal):
    def __init__(self, name, sound, animal):
        super().__init__(name, sound)
        self.can_swim = True
        self.animal = animal
    
    '''override parent class method'''
    def make_sound(self):
        if self.can_swim == False:
            print(f"{self.name} is a {self.animal} makes {self.sound} and can swim")
        else:
            cannot_swim = f"\n{self.name} is a {self.animal} makes {self.sound} and..."
            cannot_swim += f"OMG Freya noooo... {self.name} cannot swim anymore\n"
            print(cannot_swim)


dog = Animal('Dog', 'woof')
dog.make_sound()

german_shepherd = Dog('Zeus', 'woof', breed='German Shepherd')
german_shepherd.make_sound()

grey_cat = Cat('Freya', 'meow', color='grey', animal='cat')
grey_cat.make_sound()

tweety = Bird('Tweety', 'squawk')
tweety.make_sound()

fishy = Fish('Nemo', 'bloob', animal='Fish')
fishy.make_sound()
