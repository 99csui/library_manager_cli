from book import Book

class Library:

    def __init__(self):
        self.books = []

    
    def add_book(self, book):
        if isinstance(book,Book):
            if book in self.books:
                return False
            self.books.append(book)
            return True
        else:
            return False



    def find_book_by_id(self, book_id):
        for book in self.books:
            if book_id == book.id:
                return book
            
        return None



    def remove_book(self,book_id):
        for book in self.books:
            if book_id == book.id:
                self.books.remove(book)
                return True
            
        return False



    def list_books(self):
        return self.books



    def borrow_book(self, book_id):
        founded_book = self.find_book_by_id(book_id)
        if founded_book is None:
            return None
        return founded_book.borrow()
        


    def return_book(self, book_id):
        founded_book = self.find_book_by_id(book_id)
        if founded_book is None:
            return None
        return founded_book.return_book()


