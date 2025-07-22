class Book():
    def __init__(self, title, author, publication_year,isbn,availability_status):
        self.__title = title
        self.author = author
        self.publication_year = publication_year
        self.__isbn = isbn
        self.availability_status = availability_status
    
    def get_book_info(self):
        if (self.availability_status == True):
            status = "Available"
        else:
            status = "Not Available"
        txt = f"Title : {self.title}\nAuthor : {self.author}\nPublication Year : {self.publication_year}\nISBN : {self.isbn}\nAvailability Status : {status}"
        return txt
    
    def update_availability(self, status):
        self.availability_status = status
    
    def getISBN(self):
        return self.__isbn
    
    def setISBN(self,isbn):
        #isbn ="388439"
        if (isbn.__len__ != 13):
            print("ISBN should be 13 digits long.")
        else:
            self.__isbn = isbn






    def __str__(self):
        return self.title
    


if __name__ == "__main__":
    book1 = BOOK('xy','zk',2009,9845,True)
    print(book1.get_book_info())