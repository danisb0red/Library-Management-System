from person import Person
from book import Book

class LibraryUser(Person):
  def __init__(self,name, email, user_id, borrowed_books):
    super.__init__(name,email)
    self.user_id = user_id
    self.borrowed_books = borrowed_books 

  def borrow_book(self, book : Book):
    self.borrowed_books.append(book)
    book.update_availability(False)

  def return_book(self, book:Book):
    self.borrowed_books.remove(book)
    book.update_availability(True)

