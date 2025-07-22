from book import Book
class Library():
 
   books_list = books_list
    
   def isAvailable(isbn):
      #check if the book with such isbn is in the lib
      #if it is then check if its available 
      #book1 = BOOK("huh","hi",2009,9845,True)
      #book2 = BOOK("hmi","ib",2015,9455,True) 
      #self.books_list = [book1,book2]
      for temp_book in books_list:
         if temp_book.isbn == isbn:
            if temp_book.availability_status == True:
               return True
      return False
    
   def add_book(book):
      if book not in books_list:
          books_list.append(book)

   def search_book(isbn):
      for temp_book in books_list:
         if temp_book.isbn == isbn:
            return temp_book
      
      
      

if __name__ == "__main__":
    book1 = BOOK("huh","hi",2009,9845,True)
    book2 = BOOK("hmi","ib",2015,9455,False) 
    books_list = [book1,book2]
  #  lib1 = LIBRARY(books_list)
    #print(lib1.isAvailable(9845))
    #print(lib1.isAvailable(98))
    #print(lib1.isAvailable(9455))
    book3 = BOOK("i","i",2005,9355,False) 
   # lib1.add_book(book3)
    #for x in lib1.books_list:
     #  print(x)

#    lib1.add_book(book2)
 #   for x in lib1.books_list:
  #     print(x)
