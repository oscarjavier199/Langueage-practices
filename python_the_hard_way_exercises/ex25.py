
#this function will break words for us.
def break_words(stuff):
    words = stuff.split(" ") #The split() method splits a string into a list, the default separator is any whitespace
    return words

#this function will sort the words
def sort_words(words):
    return sorted(words) #The sorted() function returns a sorted list of the specified iterable object.

#this function will print the first word after popping it off
def print_first_word(words):
    words = words.pop(0) #The pop() method removes the element at the specified position.
    
#this function will print the last word after popping it off
def print_last_word(words):
    word = words.pop(-1)
    print(word)
    
#takes a full sentence and return the sorted words    
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

#prints the first and last words of the sentence
def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
#sorts the words then prints the first and last one
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    

    

