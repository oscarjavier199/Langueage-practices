#making an argument optional:

#middle_name='' is our optional argument
def name(first_name, last_name, middle_name=''):
    
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

person = name('oscar', middle_name='javier', last_name='perez')
print(person)

person = name('jack', 'sparrow')
print(person)