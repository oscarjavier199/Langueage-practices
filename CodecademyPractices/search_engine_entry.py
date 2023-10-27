class SearchEngineEntry:
    secure_prefix = "https://"
    def __init__(self, url):
        self.url = url

    def secure(self):
        return f"{self.secure_prefix}{self.url}"

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry('www.wikipedia.org')

print(codecademy.secure())
print(wikipedia.secure())

print("*" * 25)

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    self.diameter = diameter

    print(f"Creating circle with diameter {self.diameter}")
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    circumference = 2 * self.pi * self.radius
    return circumference

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())


