from person import Person
from book import Book
from library import Library
from libraryItem import LibraryItem
from magazine import Magazine
import datetime
class LibraryStaff(Person):
    
    def __init__(self,name,email,user_id, borrowed_books,borrowed_magazines):
        super().__init__(name,email,user_id,borrowed_books,borrowed_magazines)
        #self.user_id = user_id
        #self.borrowed_books = borrowed_books
        #self.borrowed_magazines = borrowed_magazines
    
    def add_item(self, item:LibraryItem):
        Library.add_item( item,item.type)
        print("\nAdded ", item.get_item_info())


    def remove_item(self, item:LibraryItem):
        if (item.type == "Book"):
            book = item
            if book.availability_status == False:
               print("Book not available.")
            else:
             if (book in Library.books_list):
              Library.books_list.remove(book)
              print(book.getTitle()," removed.")

        elif (item.type == "Magazine"):
            mag = item
            if book.availability_status == False:
               print("Magazine not available.")
            else:
             if (mag in Library.magazines_list):
                Library.magazines_list.remove(mag)
                print(mag.getTitle()," removed.")
  


    def borrow_item(self, item : LibraryItem):
     if (item.type == "Book"):
        book = item
        self.borrowed_books.append(book)
        book.update_availability(False)
        print(self.name, " Borrowed ",book.getTitle(),"\n")
        x = datetime.date.today()
        book.set_borrow_date(x)
     elif (item.type == "Magazine"):
        mag = item
        self.borrowed_magazines.append(mag)
        mag.update_availability(False)
        print(self.name, " Borrowed ",mag.getTitle(),"\n")
        y = datetime.date.today()
        mag.set_borrow_date(y)

    
   
   # def update_book(book:Book):
    #    temp_isbn = book.getISBN
     #   temp_book = Library.search_book(temp_isbn)
      #  Library.books_list.remove(temp_book)
       # Library.books_list.append(book)
