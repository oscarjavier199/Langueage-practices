class Circle:
    """Class to claculate the area of a circle"""

    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2

circle = Circle()

pizza_area = 12
teaching_table = 36
round_room = 11460

print(circle.area(pizza_area / 2))
print(circle.area(teaching_table / 2))
print(circle.area(round_room / 2))