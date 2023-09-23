people = {"Oscar": 23,

"alex":  68,

"Maxence": 27,

"Lasse": 100,

"Mike": 44}



Age = {23: "young",

68: "elderly",

27: "inmature",

100: "old",

44: "mature"}


for name, age in list(people.items()):
    print(f"{name} is {age} years old")

print(f"my friend Alex is: ", people["alex"])
print(f"My friend Mike is:", people["Mike"])

for number, age_opinion in Age.items():
    print(f"Do you think that {number} is too {age_opinion}?")



people_animals = {"oscar": "cats", 
                  "charlie": "cats",
                  "Thor": "goats",
                  "Odin": "wolfs",
                  "Freya": "cats",

}

for human, animal in people_animals.items():
    print(f"{human} prefers {animal} than any other animal in the world!")