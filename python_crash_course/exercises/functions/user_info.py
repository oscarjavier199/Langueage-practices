def user(name, last, **user_info):
    
    user_info['First name'] = name
    user_info['Last Name'] = last
    return user_info

user_0 = user('Bruce', 'Wayne',
              location='Gotham',
              field='Multimillionaire', 
              social='None'
              )
print(user_0)


user_1 =user('Jhon', 'Wick',
             location='New York', 
             field='unknown',
             pets='None'
             )
print(user_1)