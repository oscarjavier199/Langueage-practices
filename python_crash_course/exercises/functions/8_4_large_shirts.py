#function definition and function call using default parameters

print("\nFirst shirt:")

def shirt(size='large', message='I ❤️  python'):
    print(f"\n\tYour shirt is size: {size.title()} \n\tThe message is: {message.title()}\n")
    
shirt()
print("\nSecond Shirt: ")
shirt(size='medium')
print("\nThird shirt:")
shirt(size='small', message='I ❤️  SQL')