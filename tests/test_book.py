import unittest
from book import Book


class TestBook(unittest.TestCase):

    def test_borrow_change_available_to_false(self):
        book = Book(1,"Clean Code","Robert C. Martin",True)
        Book.borrow(book)

        self.assertFalse(book.available)


    def test_borrow_return_false_if_book_is_borrowed(self):
        book = Book(1,"Clean Code","Robert C. Martin",False)
        result = Book.borrow(book)

        self.assertFalse(result)


    def test_return_book_change_availability_to_true(self):
        book = Book(1,"Clean Code","Robert C. Martin",False)
        Book.return_book(book)

        self.assertTrue(book.available)


    def test_return_book_return_false_if_book_is_available(self):
        book = Book(1,"Clean Code","Robert C. Martin",True)
        result = Book.return_book(book)

        self.assertFalse(result)


