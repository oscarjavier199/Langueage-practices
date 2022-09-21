vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Type here any word: ")
print("The Vowels in the word you entered are:")

for letter in word:
     if letter in vowels:
         print(letter)
         
#program will check which vowels are in an input taken from the user