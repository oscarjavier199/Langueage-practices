# program will let us know the area of certain given objects

class Circle:
    pi = 3.14
    def area(self, radius):
        return Circle.pi * radius ** 2

circle = Circle()

pizza_area = circle.area (12/2)
teaching_table_area = circle.area (36/2)
round_room_area = circle.area (11460)

print("Pizza Area:", pizza_area, "\nTeaching Table Area:", teaching_table_area, "\nRound Room Area:", round_room_area)
