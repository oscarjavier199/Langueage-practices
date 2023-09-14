#program will take an int as input from user (in kilograms) 
#and then output the equivalent number in joules

def main():
    formula()
    
def formula():
    m = int(input("Please enter the mass (in Kilograms): \nm: ")) #asks user for int (kilograms)
    e = 90000000000000000 #equivalent of 1kl in joules
    print("E:", m * e) #prints the result of m * e
    
if __name__ == "__main__":
    main()