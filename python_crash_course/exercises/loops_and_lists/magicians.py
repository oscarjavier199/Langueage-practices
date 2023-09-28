magicians = ['alice', 'david', 'caroline', 'oscar', 'charlie', 'alex', 'harry']

#for every magician in the list of magicians, print the magician's name
for magician in magicians:
    print(f'{magician.title()} that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}\n")

print(f"\n**the first three items in the list are {magicians[0:3]}")
print(f"\n**Three items from the middle of the list are: {magicians[2:5]}")
print(f"\n**The last three items in the list are: {magicians[-3:]}")

print('\nThank you, everyone.  That was a great magic show!')