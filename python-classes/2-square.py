"""
This module is a definition of a class Square .
"""
class Square():
    """
    A class that represents a square
    
    Attributes:
        size(int): The size of the square

    Methods:
        __init__(self, size): Initializes a Square object with the given size.
        area: Returns the area of the square
    """

    def __init__(self, size=0):
        """Initialize a square instance
            Args:
                size(int): the size of the square initialized to 0
                """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size  < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Method that computes area of the square
        """
        sq_area = self.__size ** 2
        return sq_area    