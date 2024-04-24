#!/usr/bin/python3
"""define a square"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
        """initalize a square
        args:
            size(int): the size of a square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
