from person import Person
from book import Book
from library import Library
class LibraryStaff(Person):
    
    def __init__(self,name,email,user_id, borrowed_books):
        super().__init__(name,email)
        self.user_id = user_id
        self.borrowed_books = borrowed_books
    
    def add_book(book:Book):
        Library.add_book(book)

    def remove_book(book:Book):
        if (book in Library.books_list):
            Library.books_list.remove(book)

    def update_book(book:Book):
        temp_isbn = book.getISBN
        temp_book = Library.search_book(temp_isbn)
        Library.books_list.remove(temp_book)
        Library.books_list.append(book)

    def borrow_book(self, book : Book):
        self.borrowed_books.append(book)
        book.update_availability(False)
        print("\nStaff ", self.name, " Borrowed ",book.getTitle())