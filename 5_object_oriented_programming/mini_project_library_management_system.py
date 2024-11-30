class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' issued.")
                return
        print(f"Book '{title}' not available.")

    def return_book(self, title, author):
        self.add_book(title, author)
        print(f"Book '{title}' by {author} returned.")

    def list_books(self):
        print("Books in library:")
        for book in self.books:
            print(f"{book.title} by {book.author}")

library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.list_books()
library.issue_book("The Great Gatsby")
library.return_book("The Great Gatsby", "F. Scott Fitzgerald")
library.list_books()
