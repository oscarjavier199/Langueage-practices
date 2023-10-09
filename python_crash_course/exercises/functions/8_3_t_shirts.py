#program defines a function that takes two parameters and then calls the function:

def make_shirt(size, message):
    print("\n\tThank you for ordering from our site! ❤️")
    print(f"\n\tYour T-shirt will be size: {size.title()}")
    print(f"\n\tThe message printed on it will be: \n\t'{message.title()}'\n")
    
make_shirt(size='medium', message='Everyday is a second chance!')
print("*" * 50)
make_shirt('large', 'buy now, regret later')
    