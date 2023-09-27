#practice for zip(), program will take two lists and combine them into one
owners = ["oscar", "alex", "meredith", "christina", "charles"]
dog_names = ["ralph", "gandalf", "carter", "larry", "harry"]

owners_and_dogs = zip(owners, dog_names)

list_owners_dogs = list(owners_and_dogs)
print(list_owners_dogs)