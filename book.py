class Book:

    def __init__(self, id, title, author, available):
        self.id = id
        self.title = title
        self.author = author
        self.available = True

    
    def borrow(self):
        if self.available:
            self.available = False
        else:
            return False
        

    def return_book(self):
        if not self.available:
            self.available = True
        else:
            return False


    def __str__(self):
        return f"Book\n Id: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nAvailable: {self.available}"

    def __eq__(self, other):
        if not isinstance(other,Book):
            return False
        return self.id == other.id

