from book import Book
from library import Library


book1 = Book(1,"Clean Code","Robert C. Martin")
book2 = Book(2,"Python Crash Course","Eric Matthes")

library = Library()

library.add_book(book1)

print(library.books)

