from book import Book
#from person import Person
#from libraryStaff import LibraryStaff
#from libraryUser import LibraryUser

class Library():
    
   magazines_list = [] 
   books_list = []
  
    
   def isAvailable(type, id):
      #check if the book or mag with such isbn is in the lib
      #if it is then check if its available 
      #book1 = BOOK("huh","hi",2009,9845,True)
      #book2 = BOOK("hmi","ib",2015,9455,True) 
      #self.books_list = [book1,book2]

      if(type == "Book"):
       for temp_book in Library.books_list:
         if temp_book.getISBN() == id:
            if temp_book.availability_status == True:
               return True
       return False
      elif(type =="Magazine"):
         for temp_mag in Library.magazines_list:
            if temp_mag.getISSN() == id:
             if temp_mag.availability_status == True:
                  return True
         return False

    
   def add_item(item, type):
      if (type == "Book"):
         if item not in Library.books_list:
             Library.books_list.append(item)
      elif (type == "Magazine"):
        if item not in Library.magazines_list:
             Library.magazines_list.append(item) 

   def search_item(type, id):
      if (type == "Book"):
         for temp_book in Library.books_list:
            if temp_book.getISBN() == id:
               return temp_book
      elif (type == "Magazine"):
            for temp_mag in Library.magazines_list:
             if temp_mag.getISSN() == id:
                return temp_mag

         
   def set_booksList(temp_books_list):
       Library.books_list = temp_books_list

   def set_magazinesList(temp_magazines_list):
       Library.magazines_list = temp_magazines_list
    
   def show_library():
    if (len(Library.books_list)==0):
      print("No Books in Library")
    else:
        print("Books :\n")
        for temp_book in Library.books_list:
         print("Title: ",temp_book.getTitle()," Status:", "available" if temp_book.availability_status else "not available", "ISBN : ", temp_book.getISBN())
         print("\n")
    if (len(Library.magazines_list)==0):
      print("No Magazines in Library\n")
    else:
      print("Magazines :\n")
      for temp_mag in Library.magazines_list:
         print("Title: ",temp_mag.getTitle()," Status:", "available" if temp_mag.availability_status else "not available","ISSN : ", temp_mag.getISSN())
         print("\n")
      
      
    
      
'''
if __name__ == "__main__":
    book1 = Book("bat","hi",2009,9845,True)
    book2 = Book("cat","ib",2015,9455,False)
    book3 = Book("cat","ib",2015,9455,False) 
    book4 = Book("cat","ib",2015,9455,False)
    book5 = Book("cat","ib",2015,9455,True)
    book6 = Book("cat","ib",2015,9455,True)
    temp_books = [book1,book2,book3,book4,book5,book6]
    Library.set_booksList(temp_books)
    user = LibraryUser("Bruce","stuff",9592,[book2,book4])
    staff = LibraryStaff("Bob","huh",944,[book3])
    Library.show_library()
    user.borrow_book(book1)
    Library.show_library
    staff.borrow_book(book6)
    Library.show_library()
    print("Staff borrowing unavailable book test : \n")
    staff.borrow_book(book4)
    Library.show_library()
    print("User borrowing unavailable book test : \n")
    user.borrow_book(book3)
    Library.show_library()
'''
