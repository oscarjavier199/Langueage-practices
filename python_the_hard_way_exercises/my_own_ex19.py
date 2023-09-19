#simple program to define a variable with arguments and assign values to those arguments

def tipping(dinner_price, tip_amount): #define variable with 2 arguments
    print("your dinner was %r and you should tip %r\n" %(dinner_price, tip_amount)) #prints message using the two arguments
    
tipping("$50.00", "$15.00") #gives the value of the two arguments defined in the tipping function

print("But if you eat dessert: ") #prints message
dessert_meal=("$75.00") #new variable with value $75.00
dessert_tip=("$17.00") #new variable with value $17.00
tipping(dessert_meal, dessert_tip) #assigns the new variables dessert_meal and dessert_tip to our function and as the values for the two arguments

print("or you could leave no tip 😐") #prints message
tipping("$50.00", "$00.00") #assigns this values to the arguments given in the function