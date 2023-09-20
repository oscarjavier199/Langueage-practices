#program will decode and encode a given file, for this exercise the file is called language.txt

import sys #imports sys

script, input_encoding, error = sys.argv #assigns three arguments to argv

def main(language_file, encoding, errors): #main function with 3 parameters
    line = language_file.readline() #reads a line of the file that is given
    
    if line: #if statement to check if there is any data in the line we got in line 6, if there is no data it would skip line 9 and 10
        print_line(line, encoding, errors) #prints the line
        return main(language_file, encoding, errors) #we call main inside main, that would make a loop, until there is no data in a line, then it would stop
    
def print_line(line, encoding, errors): #this function encodes each line from languages.txt (or the file we give to the program)
    next_lang = line.strip() #stip() will get rid of any spaces at the beginning or the end of the line
    raw_bytes = next_lang.encode(encoding, errors=errors) #next_lang is a string, we need to get the raw bytes, so we must call .encode() to encode strings, we pass to encoding we want and how to handle errors
    cooked_string = raw_bytes.decode(encoding, errors=errors) #decode() will get a python string, it should be the same as the next_lang variable from previous line. 
    
    print(raw_bytes, "<===>", cooked_string) #we print both variables (next_lang and raw_bytes)
    
languages = open("languages.txt", encoding="utf-8") #open the file we want

main(languages, input_encoding, error) #calling the main function with the right parameters