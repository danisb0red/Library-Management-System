from book import Book
from magazine import Magazine
from library import Library
from libraryStaff import LibraryStaff
from libraryUser import LibraryUser

if __name__ == "__main__":

    print("********************************")
    print("********************************")
    print("Library Management System")
    print("********************************")
    print("********************************")
    print('\n' )
    end = False
    while (end != True):

     choice = input("Enter 1 to start as a User or 2 to start as a Staff member : ")

     if (choice == "1"):
        name = input("Enter your name: ")
        user = LibraryUser(name,"tempmail","tempid",[],[])
        print("Weclome User !")
        choice2 = ""
       
        endloop = False
        while (endloop != True):
         print('''
            1. Show Items List In The Library
            2. Show Items User has borrowed
            3. Borrow a Book  
            4. Return a Book
            5. Borrow a Magazine
            6. Return a Magazine
            7. End
            8. Switch To Staff
                  ''')
        
         choice2 = input("Enter your choice :")
       
           
         match choice2:
           case "1":
              Library.show_library()
           case "2":
               user.show_items()
           case "3":
               temp = input("Enter the ISBN of the Book You Want to Borrow :")
               tempbook = Library.search_item("Book",temp)
               if (tempbook == None):
                  print("Book not found")
               else:  
                    user.borrow_item(tempbook)
           case "4":
               tempr = input("Enter the ISBN of the Book You Want to Return :")
               tempbookr = Library.search_item("Book",tempr)
               if (tempbookr == None):
                   print("Book Not Found")
               else:
                  user.return_book(tempbookr)
           case "5":
               tempm = input("Enter the ISSN of the Magazine You Want to Borrow :")
               tempmag = Library.search_item("Magazine",tempm)
               if (tempmag == None):
                  print("Magazine not found")
               else:  
                    user.borrow_item(tempmag)

           case "6":
                temprm = input("Enter the ISSN of the Magazine You Want to Return :")
                tempmagr = Library.search_item("Magazine",temprm)
                if (tempmagr == None):
                    print("Magazine Not Found")
                else:
                 user.return_magazine(tempmagr)
           case "7":
                 end = True
                 endloop = True
           case "8":
                  end = False
                  endloop = True

        if end == True:
              break
        
        

            
       # exit;  
               
               
              
              
            
        #User UI and stuff

     elif choice == "2" :
        name = input("Enter your name: ")
        staff = LibraryStaff(name,"tempmail","tempid",[],[])
        print("Weclome Staff Member")
        choice2 = ""
        while (choice2 != "12"):
         print('''
            1. Show Items List In The Library
            2. Show Items Staff has borrowed
            3. Borrow a Book  
            4. Return a Book
            5. Borrow a Magazine
            6. Return a Magazine
            7. Add a Book to Library
            8. Remove a Book from Library
            9. Add a Magazine to Library
            10. Remove a Magazine from Library
            11. End
            12. Switch To User
            13. Create Library Report
                  ''')
        
         choice2 = input("Enter your choice :")
       
           
         match choice2:
           case "1":
              Library.show_library()
           case "2":
               staff.show_items()
           case "3":
               temp = input("Enter the ISBN of the Book You Want to Borrow :")
               tempbook = Library.search_item("Book",temp)
               if (tempbook == None):
                  print("Book not found")
               else:  
                    staff.borrow_item(tempbook)
           case "4":
               tempr = input("Enter the ISBN of the Book You Want to Return :")
               tempbookr = Library.search_item("Book",tempr)
               if (tempbookr == None):
                   print("Book not found")
               else:
                    staff.return_book(tempbookr)
           case "5":
               tempm = input("Enter the ISSN of the Magazine You Want to Borrow :")
               tempmag = Library.search_item("Magazine",tempm)
               if (tempmag == None):
                  print("Magazine not found")
               else:  
                    staff.borrow_item(tempmag)
           case "6":
                temprm = input("Enter the ISSN of the Magazine You Want to Return :")
                tempmagr = Library.search_item("Magazine",temprm)
                if (tempmagr == None):
                    print("Magazine not found")
                else:
                 staff.return_magazine(tempmagr)
           case "7":
               title = input("Enter the title of the Book : ")
               author = input("Enter the author of the Book : ") 
               pub_year = input("Enter the publication year of the Book : ")
              # isbn = input("Enter the ISBN of the Book : ")2
              
               tempBook = Book(title,author,pub_year,82,True)
               staff.add_item(tempBook)
           case "8": 
               targtemp = input("Enter the ISBN of the Book you want to remove: ")
               remBook = Library.search_item("Book",targtemp)
               staff.remove_item(remBook)
           case "9":
               title = input("Enter the title of the Magazine : ")
               #author = input("Enter the author of the Book : ") 
               pub_year = input("Enter the publication year of the Magazine: ")
             #  issn = input("Enter the ISSN of the Magazine : ")
               #tempBook = Book(title,author,pub_year,isbn,True)
               tempMag = Magazine(title,pub_year,92,True)
               staff.add_item(tempMag) 
           case "10":
               targtempm = input("Enter the ISSN of the Magazine you want to remove: ")
               remMag = Library.search_item("Magazine",targtempm)
               staff.remove_item(remMag) 
           case "11":
                 end = True
                 break
           case "13":
                 Library.create_book_report()

        #exit;   
    #else:
     #   while (choice != "1" or choice != "2"):
      #   choice = input("Enter 1 to start as a User or 2 to start as a Staff member :") 


          





'''
book1 = Book("bat","hi",2009,9845,True)
book2 = Book("cat","ib",2002,9455,False)
    book3 = Book("igor","ib",2015,9467,False) 
    book4 = Book("dttg","ib",2025,9496,False)
    book5 = Book("clips","ib",2002,9585,True)
    book6 = Book("gnx","ib",2023,99235,True)
    mag1 = Magazine("Nwes",2003,7837,True)
    mag2 = Magazine("Cha",2006,8787,True)
    temp_books = [book1,book2,book3,book4,book5,book6]
    temp_mags = [mag1,mag2]
    Library.set_booksList(temp_books)
    Library.set_magazinesList(temp_mags)
    print(Library.search_item("Book",9496))
    print(Library.search_item("Magazine",7837))
    
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