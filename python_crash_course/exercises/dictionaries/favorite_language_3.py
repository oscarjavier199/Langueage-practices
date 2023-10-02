favorite_languages = {
    'jen': 'python', 
    'edward': 'c',
    'mike': 'ruby', 
    'charles': 'python',
    'xavier': 'c#',
    'magneto': 'SQL',
}

poll_taken = ['jen', 'edward', 'mike']

for people in favorite_languages.keys():
    if people in poll_taken:
        print(f"{people.title()}, Thank you for taking the poll, you are the best!")
    if people not in poll_taken:
        print(f'''\nI see you haven\'t taken the poll! {people.title()}, 
I seriously suggest you to take the poll''')