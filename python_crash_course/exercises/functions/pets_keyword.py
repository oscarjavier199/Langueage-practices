#program defines a function and passes two parameters
#then in the function call gives two arguments using keywords

#! keyword argument:

def book(author, title):
    print(f"The last book I read was {title.title()} from {author.title()}")
    
book(title = 'Harry Potter', author = 'J.K. Rowling')