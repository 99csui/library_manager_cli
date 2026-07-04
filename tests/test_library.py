import unittest
from library import Library
from book import Book


class TestLibrary(unittest.TestCase):

    def test_library_start_with_empty_books(self):
        library = Library()
        result =len(library.books)
        self.assertEqual(result,0)
    
    
    def test_add_book_adds_valid_book(self ):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        result = library.add_book(book)

        self.assertEqual(len(library.books),1)


    def test_add_book_returns_false_for_invalid_object(self):
        library = Library()
        book = "this is a test"
        result = library.add_book(book)

        self.assertFalse(result)


    def test_add_book_returns_false_for_duplicated_book(self):
        library = Library()
        book1 = Book(1,"Clean Code","Robert C. Martin")
        book2 = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book1)
        result = library.add_book(book2)

        self.assertFalse(result)


    def test_find_book_by_id_returns_book_when_exist(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        library.add_book(book)

        result = library.find_book_by_id(1)
        self.assertEqual(result, book)


    def test_find_book_by_id_returns_none_when_not_exists(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book)
        
        result = library.find_book_by_id(2)
        self.assertIsNone(result)


    def test_borrow_book_returns_none_when_book_not_exist(self):
        library = Library()

        result = library.borrow_book(1)

        self.assertIsNone(result)


    def test_borrow_book_returns_true_when_book_is_available(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book)
        result = library.borrow_book(1)

        self.assertTrue(result)
    

    def test_borrow_book_returns_false_when_book_is_alredy_borrowed(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        book.borrow()
        library.add_book(book)

        result = library.borrow_book(1)

        self.assertFalse(result)


    def test_return_book_returns_none_when_book_not_exist(self):
        library = Library()

        result = library.return_book(1)

        self.assertIsNone(result)


    def test_return_book_returns_true_when_book_is_borrowed(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        book.borrow()
        library.add_book(book)

        result = library.return_book(1)

        self.assertTrue(result)


    def test_return_book_returns_false_when_book_is_available(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book)

        result = library.return_book(1)

        self.assertFalse(result)

         
    def test_list_books_return_a_list_when_has_books(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book)

        result = library.list_books()

        self.assertIsInstance(result,list)


    def test_list_books_returns_empty_list_when_not_have_books(self):
        library = Library()
        
        result = library.list_books()

        self.assertEqual(len(result),0)


    def test_list_books_returns_added_books(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book)

        result = library.list_books()

        self.assertEqual(result[0],book)

    def test_remove_book_returns_true_when_book_is_removed(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book)

        result = library.remove_book(1)
        
        self.assertTrue(result)

    def test_remove_book_remove_book_from_books(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book)
        library.remove_book(1)
        
        result = library.find_book_by_id(1)

        self.assertIsNone(result)

    def test_remove_book_returns_false_when_book_not_exist(self):
        library = Library()
        book = Book(1,"Clean Code","Robert C. Martin")
        
        library.add_book(book)

        result = library.remove_book(2)

        self.assertFalse(result)