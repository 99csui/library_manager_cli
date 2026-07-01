import unittest
from book import Book


class TestBook(unittest.TestCase):

    def test_borrow_change_available_to_false(self):
        book = Book(1,"Clean Code","Robert C. Martin")
        book.borrow()

        self.assertFalse(book.available)


    def test_borrow_return_false_if_book_is_borrowed(self):
        book = Book(1,"Clean Code","Robert C. Martin")
        book.borrow()
        result = book.borrow()

        self.assertFalse(result)


    def test_return_book_change_availability_to_true(self):
        book = Book(1,"Clean Code","Robert C. Martin")
        book.borrow()

        book.return_book()

        self.assertTrue(book.available)


    def test_return_book_return_false_if_book_is_available(self):
        book = Book(1,"Clean Code","Robert C. Martin")
        result = book.return_book()

        self.assertFalse(result)


    def test_books_are_equal_when_have_same_id(self):
        book1 = Book(1,"Clean Code","Robert C. Martin")
        book2 = Book(1,"Python Crash Course","Eric Matthes")

        result = book1 == book2

        self.assertTrue(result)

    def test_str_returns_redable_book_info(self):
        book = Book(1,"Clean Code","Robert C. Martin")

        result = str(book)

        compare_text = (f"Book\n"
            f"Id: 1\n"
            f"Title: Clean Code\n"
            f"Author: Robert C. Martin\n"
            f"Available: {True}")

        self.assertEqual(result,compare_text)
        
