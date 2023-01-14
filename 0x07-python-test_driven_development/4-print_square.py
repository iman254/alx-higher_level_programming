#!/usr/bin/python3

"""function that prints a square with the character #"""

def print_square(size):
    """function takes in size as parameter to print out a square"""
    arg:
    size - the size of the square

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i on range(0, size):
            for m in range(size):
                print("#", end="") 
