from libraryItem import LibraryItem
class Book(LibraryItem):
    def __init__(self, title, author, publication_year,isbn,availability_status):
        super().__init__("Book")
        self.__title = title
        self.author = author
        self.publication_year = publication_year
       #self.__isbn = isbn
        self.__isbn = LibraryItem.generate_random_string()
        self.availability_status = availability_status
    
    def get_item_info(self):
        if (self.availability_status == True):
            status = "Available"
        else:
            status = "Not Available"
        txt = f"Title : {self.getTitle()}\nAuthor : {self.author}\nPublication Year : {self.publication_year}\nISBN : {self.getISBN()}\nAvailability Status : {status}"
        return txt
    
   
    
    def getISBN(self):
        return self.__isbn
    
    def setISBN(self,isbn):
        #isbn ="388439"
        if (isbn.__len__ != 13):
            print("ISBN should be 13 digits long.")
        else:
            self.__isbn = isbn

    def getTitle(self):
        return self.__title
    


#if __name__ == "__main__":
   # book1 = BK('xy','zk',2009,9845,True)
    #print(book1.get_book_info())