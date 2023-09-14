def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", ""))
#    dollar = float(d.replace("$", ""))


def percent_to_float(p):
    return float(p.replace("%", "")) / 100 #The float division operation / is used when you want a more precise division result, as it does not round off the value to whole numbers.


if __name__ == "__main__":
    main()


