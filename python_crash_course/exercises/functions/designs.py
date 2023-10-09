#using functions to modify the content of a list

# program without functions:
'''
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
finished_design = []

while unprinted_design:
    design = unprinted_design.pop()
    print(f"Printing {design}..")
    finished_design.append(design)
    
print("\nThe following designs were printed:\n")
for finished_design in finished_design:
    print(finished_design)
'''

#same previous program but with functions:

# the first function removes items from a list, appends them to a new list
# and prints a message
def print_models(unprinted_design, finished_design):
    
    '''pops items from a list and appends them to a new list'''
    
    while unprinted_design:
        design = unprinted_design.pop()
        print(f"Printing {design}...")
        finished_design.append(design)
        
#The second function lets us know the design that were printed
def completed_models(finished_design):
    
    '''iterates through the items in the new list'''
    
    print("\nThe following models have been printed:\n")
    for finished_design in finished_design:
        print(finished_design)
    

unprinted_design = []
finished_design = []

'''
print_models(unprinted_design, finished_design)
completed_models(finished_design)
'''