class Song(object): #create class
    
    def __init__(self, lyrics): #initializing class
        self.lyrics = lyrics 
    
    def sing_me_a_song(self): #defining function
        for line in self.lyrics: #loop to iterate through lines
            print(line) #prints message
        
#assigning str to Song class
happy_bday = Song(["""
Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"""])

bulls_on_parade = Song (["""
They rally around tha family",
"With pockets full of shells"""])

dani_california = Song (["""
Gettin' born in the state of Mississippi
Poppa was a copper and her momma was a hippie
In Alabama, she would swing a hammer
Price you gotta pay when you break the panorama"""])

#calling class
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
dani_california.sing_me_a_song()