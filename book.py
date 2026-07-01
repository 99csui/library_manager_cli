class Book:

    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.available = True

    
    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
        

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        else:
            return False


    def __str__(self):
        return (
            f"Book\n"
            f"Id: {self.id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Available: {self.available}"
        )

    def __eq__(self, other):
        if not isinstance(other,Book):
            return False
        return self.id == other.id

