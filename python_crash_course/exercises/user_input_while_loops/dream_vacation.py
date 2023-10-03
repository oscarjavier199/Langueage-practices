dream_vacations = {}

poll_active = True

while poll_active:
    name = input("What is your name? >>> ")
    location = input("If you could go anywhere in the world, where would you go? >>> ")
    dream_vacations[name] = location
    
    repeat = input("Would you like to send this poll to your friends? (yes/no) >>> ")
    if repeat == 'no':
        poll = False


print("\n--- Result of Poll ---")
for name, location in dream_vacations.items():
    print(f"{name}, Dream destination is {location}")