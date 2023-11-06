# program shows the use of yield instead of return
def class_standing_generator():
    yield "Freshman"
    yield "Sophomore"
    yield "Junior"
    yield "Senior"


class_standings = class_standing_generator()
for class_standing in class_standings:
    print(class_standing)
