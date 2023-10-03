sandwich_orders = ['American', 'pastrami', 'BLT', 'pastrami', 'Bologna', 
                   'cheese', 'turkey', 'peanut butter and jelly', 'pastrami']
finished_sandwiches = []
print("\n\tSorry! we run out of Pastrami😒\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    ready = sandwich_orders.pop()
    print(f"Your {ready.title()} sandwich is done!\n...")
    finished_sandwiches.append(ready)
    
print("The following sandwiches are DONE.")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")
    
    