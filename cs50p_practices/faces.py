#program will ask user for input using :) or :( and then will return the same
#input but will replace :) or :( with the actual emojis

def main():
    faces()

def faces():
    convert = input("Type something using :) or :( \n")
    print(convert.replace(":(", "😐").replace(":)", "🙂"))


if __name__ == "__main__":
    main()