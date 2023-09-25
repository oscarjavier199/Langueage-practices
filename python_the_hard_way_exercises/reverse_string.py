# Define a function that takes a string as a parameter and returns the reversed string
def reverse_string(string):
    # Initialize an empty string
    reversed_string = ""
    # Loop through the characters of the string in reverse order
    for i in range(len(string) - 1, -1, -1):
        # Append each character to the reversed string
        reversed_string += string[i]
    # Return the reversed string
    return reversed_string

# Test the function with some examples
print(reverse_string("Hello"))
print(reverse_string("Python"))
print(reverse_string("123456789"))