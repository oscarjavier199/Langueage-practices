can_we_count_it = [{"s": False}, "sassafrass", 18, ["a", "d", "c", "s", "q"]]

for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + "has the count attribute!")
    else:
        print(str(type(element)) + "does not have the count attribute!")