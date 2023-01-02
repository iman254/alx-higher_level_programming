#!/usr/bin/python3

"""define the class square"""


class Square:
    """instantiating with def __innit__"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """get the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size mus be an integer")
        elif size < 0:
            raise ValueError("size must b >= 0")
        self.__size = value
