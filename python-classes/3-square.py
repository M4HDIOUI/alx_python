"""
kam class sqauare
"""
class Square():
    """
    A class that represents a square
    
    """

    def __init__(self, size=0):
      
        self.__size = size

    @property
    def size(self):
       
        return self.__size
    
    @size.setter
    def size(self, value):
        
        if value != int(value):
            raise TypeError("size must be an integer")
        if value  < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
      
        sq_area = self.__size ** 2
        return sq_area