from book import BOOK
class LIBRARY():
   def __init__(self, books_list):
      self.books_list = books_list
    
   def isAvailable(self,isbn):
      #check if the book with such isbn is in the lib
      #if it is then check if its available 
      #book1 = BOOK("huh","hi",2009,9845,True)
      #book2 = BOOK("hmi","ib",2015,9455,True) 
      #self.books_list = [book1,book2]
      for temp_book in self.books_list:
         if temp_book.isbn == isbn:
            if temp_book.availability_status == True:
               return True
      return False
      

if __name__ == "__main__":
    book1 = BOOK("huh","hi",2009,9845,True)
    book2 = BOOK("hmi","ib",2015,9455,False) 
    books_list = [book1,book2]
    lib1 = LIBRARY(books_list)
    print(lib1.isAvailable(9845))
    print(lib1.isAvailable(98))
    print(lib1.isAvailable(9455))
