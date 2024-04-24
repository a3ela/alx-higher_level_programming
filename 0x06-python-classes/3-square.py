#!/usr/bin/python3
"""define a class square"""


class Square:
    """represent a square"""

    def __init__(self, size):
        """ initilize a new square
        args:
            size(int): the size of the newe square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
            return self.size
