#program will determine if input given is from hogwarts' gryffindor, slytherin or a muggle

#asks user for input name
name = input("What's your name? ").capitalize() #str.capitalize() recognises input from user in lower or uppercase.

#match replaces repetitive if, else code, making it easier to read

match name:
    case "Harry" | "Hermione" | "Ron": # | represents or
        print("Gryffindor")
    case "Draco" | "Crabbe" | "Goyle":
        print("Slytherin")
    case _:
        print("Ugh a muggle!")