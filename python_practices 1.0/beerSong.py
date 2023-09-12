#assign the value "bottles" to a new variable called word
word = "bottles"

#loop a specified number of times from 99 down to 
#none, use "beer_num" as the loop iteration variable
for beer_num in range(99, 0, -1):
    
#the four calls to print display the current iteration's song lyrics
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    
#check if we are on the last passed-around beer
    if beer_num == 1:

#if we are at the end of the iteration end the song lyrics
        print("No more bottles of beer on the wall.")
   
#otherwise     
    else:
        
#remeber the number of the next beer in another variable called new_num
        new_num = beer_num - 1
        
#if we are about to drink the last beer
        if new_num == 1:
            
#change the value of the varaible word so the lyrics makes sence
            word: "bottle"
            
#complete this iteration's song
        print(new_num, word, "of beer on the wall.")
        
#print a blank line
    print()