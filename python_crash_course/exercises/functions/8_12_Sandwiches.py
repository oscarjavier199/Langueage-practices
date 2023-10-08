# function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides

def making_sandwiches(*items):
    print("\nAdding the following items to your sandwich: \n")
    
    for item in items:
        print(f"--{item.title()}")
    
    print("\nYour sandwich is done, enjoy it!\n")
        
making_sandwiches('lettuce', 'Turkey', 'onion', 'tomato')
print("..." * 20)

making_sandwiches('peanut butter', 'jelly')
print("..." * 20)

making_sandwiches('tuna')