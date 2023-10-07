#using functions to modify the content of a list

# program without functions:
'''
unprinted_desings = ['phone case', 'robot pendant', 'dodecahedron']
finished_desings = []

while unprinted_desings:
    desings = unprinted_desings.pop()
    print(f"Printing {desings}..")
    finished_desings.append(desings)
    
print("\nThe following designs were printed:\n")
for finished_design in finished_desings:
    print(finished_design)
'''

#same previous prgram but with functions:

# the first function removes items from a list, appends them to a new list
# and prints a message
def print_models(unprinted_desings, finished_desings):
    
    while unprinted_desings:
        desings = unprinted_desings.pop()
        print(f"Printing {desings}...")
        finished_desings.append(desings)
        
#The second function lets us know the desings that were printed
def completed_models(finished_desings):
    print("\nThe fllowing models have been printed:\n")
    for finished_desing in finished_desings:
        print(finished_desing)
    

unprinted_desings = ['phone case', 'robot pendant', 'dodecahedron']
finished_desings = []

print_models(unprinted_desings, finished_desings)
completed_models(finished_desings)