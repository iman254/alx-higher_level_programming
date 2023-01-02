#!/usr/bin/python3

"""defining a class Square."""


class Square:
    """instantiate with __init__(self, size=0)"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """public instance def area(self)"""
    def area(self):
        """return the current area of the square"""
        return (self.__size * self.__size)
