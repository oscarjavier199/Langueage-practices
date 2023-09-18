def main():
    
    user_input = input("Input: ") #get user input

    no_vowels = shorten(user_input) #remove vowels:

    print("Output: " + no_vowels) #print output:
    

def shorten(word): #function to remove vowels

    word_no_vowels = "" #empty str
    
    for letter in word: #loop though every letter
        
        if not letter.lower() in ["a", "e", "i", "o", "u"]: #check if vowels are lowercase or uppercase:
            word_no_vowels += letter 
            
    return word_no_vowels #return the new word

if __name__ == "__main__":
    main()
