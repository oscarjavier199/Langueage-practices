guest_list = ['Harry Potter', 'Gandalf', 'ethan winters']

print(f'Dear {guest_list[0].title()}, it would be great having you for dinner tomorrow night at 9:00 pm.')
print(f'My friend {guest_list[1].title()}, please accept my invitation for dinner tomorrow night at 9:00 pm')
print(f'My dear {guest_list[2].title()}, I would love having you for dinner tomorrow night, see you at 9:00 pm.')

print("\n\tHarry Potter can't make it, we'll have to invite someone else")

new_guest = 'Rick Sanchez'
guest_list.remove('Harry Potter')
guest_list.insert(0, 'Rick Sanchez')

print(f"\nNew Invitations:")


print(f'-Dear {guest_list[0].title()}, it would be great having you for dinner tomorrow night at 9:00 pm.')
print(f'-My friend {guest_list[1].title()}, please accept my invitation for dinner tomorrow night at 9:00 pm')
print(f'-My dear {guest_list[2].title()}, I would love having you for dinner tomorrow night, see you at 9:00 pm.')

print('\n\tWe found a bigger table, time to invite more people 🔥')

guest_list.insert(0, 'Ivar the Boneless')
guest_list.insert(1, 'Kratos')
guest_list.append('Ada Wong')

print(f'\n- I hope you are well {guest_list[0].title()}, it would be a pleasure to have you tomorrow night at 9:00 pm for dinner')
print(f'- {guest_list[1].title()}, please come to dinner tomorrow night, see you soon boy.')
print(f"""- It's been so long {guest_list[5].title()} since we saw each other, since that incident in spain, remember? anyways see you tomorrow night""")

print('''\n\tThe table won't be here on time 😯
\twe can only invite two people 😭''')

removed_guest_1 = guest_list.pop(1)
print(f'\n-I am so sorry {removed_guest_1.title()} but unfortunately due to some events I will have to ask you NOT to come tomorrow night ')
removed_guest_2 = guest_list.pop(2)
print(f"-Please don't come tomorrow night {removed_guest_2.title()}, I'll explain you other day")
removed_guest_3 = guest_list.pop(3)
print(f'-You are uninvited, sorry {removed_guest_3.title()}')
removed_guest_4 = guest_list.pop()
print(f'-{removed_guest_4.title()} The date of the dinner was changer for next week')

print(f'\n-{guest_list[0].title()}, nothing to worry about you are still invited to the dinner tomorrow!')
print(f'-See you tomorrow night {guest_list[1].title()}, the dinner is still up')

#del guest_list[0]
#guest_list.remove('Rick Sanchez')
#print(guest_list)

print('The current number of guests is:', len(guest_list))