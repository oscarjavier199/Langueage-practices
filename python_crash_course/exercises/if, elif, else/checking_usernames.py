#program will take a couple of lists containing usernames, if a username from 
# new usernames is in the list of existing users it will inform that to the user

current_users = ['OSCAR999', 'DR.HOUSE1', 'DRACULA111', 'BATMAN05',
'HARLEY_LOVES_JOKER', 'ADMIN']

current_users_lower = ['oscar999', 'dr.house1', 'dracula111', 
'harley_loves_joker', 'admin']

new_users = ['OSCAR999', 'DR.HOUSE1', 'superm4n', 'hulk_smash',
'resident_of_evil4']

for new_user in new_users:
    if new_user in current_users or new_user in current_users_lower:
        print(f'''Sorry, you need to enter a new user name, {new_user} is 
already taken 🙃''')
    else:
        print(f"Congrats! {new_user} is available 🥳")
