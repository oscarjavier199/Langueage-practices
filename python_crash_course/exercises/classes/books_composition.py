class Books():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book1 = Book_1()
        self.book2 = Book_2()
        self.book3 = Book_3()
        
    def main_info(self):
        print(f"\nThe Book is titled {self.title} by {self.author}\n")


class Book_1():
    def __init__(self):
        self.chapters = 6
        self.pages = 479
        self.genre = 'Mystery'
        self.published = 1866
        
    def num_chapters(self):
        print(f"Number of chapters: {self.chapters}")
        
    def num_pages(self):
        print(f"\nNumber of pages: {self.pages}\n")
    
    def book_genre(self):
        print(f"Genre: {self.genre}\n")
        
    def date(self):
        print(f"Published in {self.published}")


class Book_2():
    def __init__(self):
        self.chapters = 12
        self.pages = 658 
        self.genre = 'Science Fiction'
        self.published = 1965
        
    def num_chapters(self):
        print(f"Number of chapters: {self.chapters}")
        
    def num_pages(self):
        print(f"\nNumber of pages: {self.pages}\n")
    
    def book_genre(self):
        print(f"Genre: {self.genre}\n")
        
    def date(self):
        print(f"Published in {self.published}")


class Book_3():
    def __init__(self):
        self.chapters = 30
        self.pages = 1248
        self.genre = 'Fiction'
        self.published = 1954
        
    def num_chapters(self):
        print(f"Number of chapters: {self.chapters}")
        
    def num_pages(self):
        print(f"\nNumber of pages: {self.pages}\n")
    
    def book_genre(self):
        print(f"Genre: {self.genre}\n")
        
    def date(self):
        print(f"Published in {self.published}")


crime_punishment = Books('Crime and Punishment', 'Fyodor Dostoevsky')
crime_punishment.main_info()
crime_punishment.book1.num_chapters()
crime_punishment.book1.num_pages()
crime_punishment.book1.book_genre()
crime_punishment.book1.date()

print("-" * 20)
dune = Books('Dune', 'Frank Herbert')
dune.main_info()
dune.book2.num_chapters()
dune.book2.num_pages()
dune.book2.book_genre()
dune.book2.date()

print("-" * 20)
tlotr= Books('The Lord of the Rings', 'J.R.R. Tolkien')
tlotr.main_info()
tlotr.book3.num_chapters()
tlotr.book3.num_pages()
tlotr.book3.book_genre()
tlotr.book3.date()