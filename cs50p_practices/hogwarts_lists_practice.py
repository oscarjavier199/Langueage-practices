#program will print the content of the list
"""""
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
"""""

#we can write the program using len() to get the length of the list and then print it
"""""
students =["Hermione", "Harry", "Ron"]
for i in range(len(students)): #using len() to get the length of the list
    print(i + 1, students[i]) # we need to use i + 1 so the output for the user starts counting from 1 and not from 0
"""


#using dictionaries (dict)
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"}, 
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "Doesn't have one :("}
]

#loop to iterate to all the items in the dictionary
for student in students:
    print("The student:",student["name"], "belongs to:", student["house"], "and the patronus is an:", student["patronus"])# prints the keys and the values of the dictionarie