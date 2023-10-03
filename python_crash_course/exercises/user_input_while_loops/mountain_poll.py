#empty dictionary to store key-value pairs
responses = {}

#flag to keep the loop running
polling_active = True

while polling_active:
    name = input("\nWhat is your name? >>> ")
    response = input("Which mountain would you like to climb someday? >>> ")
    
#stores the name as keys and response as values in dictionary (responses):
    responses[name] = response

#find out if anyone else wants to take the poll:
    repeat = input("Would you like to let another person respond? (yes/no) >>> ")
    if repeat == 'no':
#flag to stop the loop if input == no
        polling_active = False
    
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would love to climb {response} one day!")
    
print(f"\nContents of dictionary:", responses)