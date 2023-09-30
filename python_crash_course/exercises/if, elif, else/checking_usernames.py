
current_users = ['OSCAR999', 'DR.HOUSE1', 'DRACULA111', 'BATMAN05',
'HARLEY_LOVES_JOKER', 'ADMIN']

#copy of list of usernames and appends of lower case usernames
current_users_lower = current_users[:]
current_users_lower.append('oscar999')
current_users_lower.append('dr.house1')
current_users_lower.append('dracula111')
current_users_lower.append('harley_loves_joker')
current_users_lower.append('admin')

new_users = ['OSCAR999', 'DR.HOUSE1', 'superm4n', 'hulk_smash',
'resident_of_evil4']

for new_user in new_users:
    if new_user in current_users:
        print(f'''Sorry, you need to enter a new user name, {new_user} is 
already taken 🙃''')
    else:
        print(f"Congrats! {new_user} is available 🥳")
        
        

        
