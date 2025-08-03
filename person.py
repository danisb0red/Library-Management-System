from book import Book
from magazine import Magazine
import datetime
class Person():

    def __init__(self, name, email,user_id, borrowed_books, borrowed_magazines):
        self.name = name
        self.email = email
        self.user_id = user_id
        self.borrowed_books = borrowed_books
        self.borrowed_magazines = borrowed_magazines


    def return_book(self, book:Book):
     if(book in self.borrowed_books):
      self.borrowed_books.remove(book)
      book.update_availability(True)
      print(book.getTitle()," was returned.")
      x = datetime.date.today()
      book.set_return_date(x)
     else:
        print("You Did not Borrow This Book.")


    def return_magazine(self,mag: Magazine):
     if(mag in self.borrowed_magazines):

        self.borrowed_magazines.remove(mag)
        mag.update_availability(True)
        print(mag.getTitle()," was returned.")
        x = datetime.date.today()
        mag.set_return_date(x)
     else:
        print("You Did not Borrow This Magazine")
      

    def show_items(self):
        print("Books : ")
        count = 1
        for tempbook in self.borrowed_books:
                print(count,". ",tempbook.getTitle(),", ISBN :", tempbook.getISBN(),", Borrow Date :", tempbook.get_borrow_date())
                count+=1
        count =1
        print("Magazines : ")
        for tempmag in self.borrowed_magazines:
            print(count,". ",tempmag.getTitle(), ", ISSN :", tempmag.getISSN(),", Borrow Date :", tempmag.get_borrow_date())
            count+=1

    
   

    