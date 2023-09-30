usernames = []

if usernames:
    for user in usernames:
        if user == 'admin'.lower():
            print(f"Hello {user} would you like to see a status report?")
        else:
            print(f'Hello {user} thank you for logging in again!')
else:
    print("We need to find some new users! 😱")