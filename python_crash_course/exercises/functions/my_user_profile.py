# Start with a copy of user_profile.py from page 148. Build a
# profile of yourself by calling build_profile()

def user_profile(name, last_name, **users):
    
    users['First Name'] = name
    users['Last Name'] = last_name
    return users

user_1 = user_profile('oscar', 'perez', 
                      age=23, 
                      profesion='student', 
                      hair='dark brown', 
                      pets='None',
                      )

print(user_1)