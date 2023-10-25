python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# Your code below:
for topic in python_topics:
    print(f"I am learning about {topic}")


# List comprehension example

# Create a list called single_digits that consists of the numbers 0-9 (inclusive).
single_digits = []

single_digits = list(range(0, 10))
print(f"Single digits list: {single_digits}")

squares = []

# # Create a for loop that goes through single_digits and prints out each one.
for digit in single_digits:
    squares.append(digit ** 2)  # appends square value
    print(f"{digit}")
print(f"Squared numbers: {squares}\n")

# list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of
# single_digits taken to the third power.
cubes = [num ** 3 for num in single_digits]
print(f"Third power: {cubes}")
