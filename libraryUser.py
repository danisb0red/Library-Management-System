from person import Person
from book import Book
from library import Library
from magazine import Magazine
from libraryItem import LibraryItem
import datetime
class LibraryUser(Person):
  def __init__(self,name, email, user_id, borrowed_books, borrowed_magazines):
    super().__init__(name,email,user_id,borrowed_books,borrowed_magazines)
    #self.user_id = user_id
    #self.borrowed_books = borrowed_books 
    #self.borrowed_magazines = borrowed_magazines

  def borrow_item(self, item : LibraryItem):
    if (item.type == "Book"):
      book = item
      if Library.isAvailable("Book",book.getISBN()):
        self.borrowed_books.append(book)
        book.update_availability(False)
        print(" Borrowed ",book.getTitle(),"\n")
        x = datetime.date.today()
        book.set_borrow_date(x)
      else:
        print(book.getTitle()," Not Available.\n")
    elif (item.type == "Magazine"):
      mag = item
      if Library.isAvailable("Magazine",mag.getISSN()):
        self.borrowed_magazines.append(mag)
        mag.update_availability(False)
        print(self.name, " Borrowed ",mag.getTitle(),"\n")
        y = datetime.date.today()
        mag.set_borrow_date(y)

  


