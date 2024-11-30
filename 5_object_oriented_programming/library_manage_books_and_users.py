# Develop a class for a library to manage books and users
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")

library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book(book1)
library.list_books()
