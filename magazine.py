from libraryItem import LibraryItem
class Magazine(LibraryItem):
    def __init__(self, title, publication_year,issn, availability_status):
        super().__init__("Magazine")
        self.publication_year = publication_year
        self.__issn = LibraryItem.generate_random_string()
        # self.__issn = self.generate_random_string()
        self.__title = title
        self.availability_status = availability_status
    
    def get_item_info(self):
        if (self.availability_status == True):
            status = "Available"
        else:
            status = "Not Available"
        txt = f"Title : {self.getTitle()}\nPublication Year : {self.publication_year}\nISSN : {self.getISSN()}\nAvailability Status : {status}"
        return txt
    
    def getISSN(self):
        return self.__issn
    
    def setISSN(self,issn):
        #isbn ="388439"
        if (issn.__len__ != 13):
            print("ISSN should be 13 digits long.")
        else:
            self.__issn = issn

    def getTitle(self):
        return self.__title
