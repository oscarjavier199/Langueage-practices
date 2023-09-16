
#variable
user_coins = 50

while user_coins > 0: #while loop until amount due is greater than 0
   print("amount due: ", user_coins) #print the amount due
   insert_coin = int(input("insert coin: ")) #ask user to insert coin
   if insert_coin in [25, 10, 5]:#check if the inserted coins are 25, 10 or 5 cents
      user_coins -= insert_coin #subtract the amount entered by user from the variable user_coins, which was 50
      
change_owed = abs(user_coins) #abs returns the absolute value of the given number, in this case user_coins variable
print("changed owed: ", change_owed) #print the changed owed.
   
   