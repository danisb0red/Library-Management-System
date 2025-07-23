from person import Person
from book import Book
from library import Library
from magazine import Magazine
from libraryItem import LibraryItem
class LibraryUser(Person):
  def __init__(self,name, email, user_id, borrowed_books, borrowed_magazines):
    super().__init__(name,email)
    self.user_id = user_id
    self.borrowed_books = borrowed_books 
    self.borrowed_magazines = borrowed_magazines

  def borrow_item(self, item : LibraryItem):
    if (item.type == "Book"):
      book = item
      if Library.isAvailable("Book",book.getISBN()):
        self.borrowed_books.append(book)
        book.update_availability(False)
        print(" Borrowed ",book.getTitle(),"\n")
      else:
        print(book.getTitle()," Not Available.\n")
    elif (item.type == "Magazine"):
      mag = item
      if Library.isAvailable("Magazine",mag.getISSN()):
        self.borrowed_magazines.append(mag)
        mag.update_availability(False)
        print(self.name, " Borrowed ",book.getTitle(),"\n")

  def show_items(self):
    print("Books : ")
    count = 1
    for tempbook in self.borrowed_books:

      print(count,". ",tempbook.getTitle())
    count =1
    for tempmag in self.borrowed_magazines:
      print(count,". ",tempmag.getTitle())

       

  def return_book(self, book:Book):
    self.borrowed_books.remove(book)
    book.update_availability(True)
  def return_magazine(self,mag: Magazine):
    self.borrowed_magazines.remove(mag)
    mag.update_availability(True)

