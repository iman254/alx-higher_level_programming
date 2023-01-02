#!/usr/bin/python3

"""define the class square"""


class Square:
    """instantiating with def __init__"""
    def __init__(self, size=0):
        """innitialise a new square"""
        self.size = size

    @property
    def size(self):
        """get the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
