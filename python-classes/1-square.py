"""
Module of definitions class Square
"""
class Square():
    """
    A class that represents a square
    
    Attributes:
        size(int): The size of the square

    Methods:
        __init__(self, size): Initializes a Square object with the given size.
    """

    def __init__(self, size=0):
       
        if size != int(size):
            raise TypeError("size must be an integer")
        if size  < 0:
            raise ValueError("size must be >= 0")
        self.__size = size