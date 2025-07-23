from abc import ABC, abstractmethod
import random
import string
class LibraryItem(ABC):
    def __init__(self,type):
        super().__init__()
        self.type = type


    def borrow_item(self):
        pass

    def return_item(self):
        pass

    def update_availability(self, status):
        self.availability_status = status
        
    @abstractmethod
    def get_item_info(self):
        pass

    def generate_random_string():
        length = 13
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return(random_string)
    
    
