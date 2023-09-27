#program will read a cvs file and strip it so it will be easier to read.

students = []
with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") #strip() will remove the white space at the end, split will split the elements before and after a comma
        student = {"name": name, "house": house}
        students.append(student)



