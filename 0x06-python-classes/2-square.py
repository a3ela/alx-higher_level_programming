#!/usr/bin/python3
"""define a class square"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
    """ Initialize a new square
    Args:
        size(int): the size of the square
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    self.size = size
