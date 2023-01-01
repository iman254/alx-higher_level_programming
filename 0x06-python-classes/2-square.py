#!/usr/bin/python3

"""defining a class Square."""
class Square:
    """initializing attributes of the class"""
    def __init__(self, size=0):
        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise valueError("size must be >= 0")
        self.__size = size

    
