# Animal is-a object 
class Animal(object):
    pass

# Dog is-a object
class Dog(Animal):
    def __init__(self, name):
        ## has-a object
        self.name = name

# is-a object
class Cat(Animal):
    def __init__(self, name):
        ## has-a object
        self.name = name
        
# is-a object
class Person(object):
    def __init__(self, name):
        ## has-a object
        self.name = name
        ## has-a object
        self.per = None
        
# Employee is-a object
class Employee(Person):
    def __init__(self, name, salary):
        ## is-a object
        super(Employee, self).__init__(name)
        ## self.salary has-a object
        self.salary = salary
        
# Fish is-a object
class Fish(object):
    pass

# Salmon is-a object 
class Salmon(Fish):
    pass

# Halibut is-a class (object)
class Halibut(Fish):
    pass

# rover is-a dog (object)
rover = Dog("Rover")

# Thor is-a cat
Thor = Cat("Thor")

# mary is-a person (object)
mary = Person("Mary")

# mary has-a pet (object)
mary.pet = Thor

# frank has-a employee (object)
frank = Employee("Frank", 120000)

# frank has-a pet (object)
frank.per = rover

# flipper is-a fish (object)
flipper = Fish()

# crouse is-a salmon (object)
crouse = Salmon()

# harry has-a Halibut (object)
Harry = Halibut()