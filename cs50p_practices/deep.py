#program will ask "what is the answer to the Great Question of life, 
# the universe and everything?" and if the answer is  "42" or "forty-two" 
# or "forty two" or "Forty Two" will input Yes otherwise will print No

def main():
    question()
    
def question():
    life_question = input("what is the answer to the Great Question of life, the universe and everything? \n")
    if life_question == "42" or life_question == "forty-two" or life_question ==  "forty two" or life_question == "Forty Two":
        print("Yes")
    else:
        print("No")
        
if __name__ == "__main__":
    main()