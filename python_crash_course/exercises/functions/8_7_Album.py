#function takes input from user using a while loop and then prints a dict with
#the infoas key-value pairs

def album_1(singer_1, album_1, songs=None):
    album_info_1 = {'singer': singer_1, 'album': album_1}

    if songs:
        album_info_1['songs']= songs
    return album_info_1

while True:
    print("\nplease enter a singer/group or (Enter 'q' to quit)")

    singer_group = input('Singer name: ')
    if singer_group == 'q':
        break
    
    print("\nEnter an album name or (Enter 'q' to quit)")
    
    album = input("Album: ")
    if album == 'q':
        break
    
    info_1 = album_1(singer_group, album)
print(f'\n{info_1}')


'''
print("\nInformation album 1:")
info_1 = album_1('Muse', "Simulation Theory", 11)
print(info_1)

print("\nInformation album 2:")
info_1 = album_1('Green Day', "21st Century Breakdown", 'unknown')
print(info_1)

print("\nInformation album 3:")
info_1 = album_1('The Frey', "How to save a life")
print(info_1)

print("\nInformation album 4:")
info_1 = album_1('Linkin park', "One More Light", 10)
print(info_1)
'''