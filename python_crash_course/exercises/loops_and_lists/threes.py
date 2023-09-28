#list of multiples of 3, from 3 to 30, use for loop to print numbers
# # in the list

multiple_3 = []

for number in range(1, 11):
    multiple_3.append(number * 3)
print(multiple_3)


#using list comprehension:
multiple = [number * 3 for number in range(1, 11)]
print(multiple)