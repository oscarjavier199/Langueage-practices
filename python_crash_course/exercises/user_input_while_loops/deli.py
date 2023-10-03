sandwich_orders = ['American', 'BLT', 'Bologna', 'cheese', 'turkey', 
                   'peanut butter and jelly']
finished_sandwiches = []


while sandwich_orders:
    ready = sandwich_orders.pop()
    print(f"Your {ready.title()} sandwich is done!\n...")
    finished_sandwiches.append(ready)
    
print("The following sandwiches are DONE.")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")
    
    