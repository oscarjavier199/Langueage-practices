#function definition and returns a value instead of printing a message

def books(author, title):
    book = f"The book '{title.title()}' is from {author.title()}"
    return book

reading_book = books(author='J.R.R. tolkien', title='The hobbit')
print(f"\n{reading_book}\n")