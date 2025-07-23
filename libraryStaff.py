from person import Person
from book import Book
from library import Library
from libraryItem import LibraryItem
from magazine import Magazine
class LibraryStaff(Person):
    
    def __init__(self,name,email,user_id, borrowed_books,borrowed_magazines):
        super().__init__(name,email)
        self.user_id = user_id
        self.borrowed_books = borrowed_books
        self.borrowed_magazines = borrowed_magazines
    
    def add_item(self, item:LibraryItem):
        Library.add_item( item,item.type)
        print("\nAdded ", item.get_item_info())

    def remove_item(item:LibraryItem):
        if (item.type == "Book"):
            book = item
            if (book in Library.books_list):
              Library.books_list.remove(book)
              print(book.getTitle()," removed.")

        elif (item.type == "Magazine"):
            mag = item
            if (mag in Library.magazines_list):
                Library.magazines_list.remove(mag)
                print(mag.getTitle()," removed.")
  

    def update_book(book:Book):
        temp_isbn = book.getISBN
        temp_book = Library.search_book(temp_isbn)
        Library.books_list.remove(temp_book)
        Library.books_list.append(book)

    def borrow_item(self, item : LibraryItem):
     if (item.type == "Book"):
        book = item
        self.borrowed_books.append(book)
        book.update_availability(False)
        print(self.name, " Borrowed ",book.getTitle(),"\n")
     elif (item.type == "Magazine"):
        mag = item
        self.borrowed_magazines.append(mag)
        mag.update_availability(False)
        print(self.name, " Borrowed ",mag.getTitle(),"\n")

    
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
      