"""
 Printing a square
"""
class Square():
    """
    A class that represents a square
    
    Attributes:
        size(int): The size of the square

    Methods:
        __init__(self, size): Initializes a Square object with the given size.
        area: Returns the area of the square
        @property: A getter to retrieve private instance attribute
        @size.setter: A setter that sets the value to the priv. att
        my_print: Public method that prints square of #
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
    
    def my_print(self):

        if self.__size == 0:
            print()

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()