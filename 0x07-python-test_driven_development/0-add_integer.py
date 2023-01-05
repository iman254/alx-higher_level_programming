#!/usr/bin/python3

""" Function that adds 2 integers."""


def add_integer(a, b=98):
    """Function that sums two integers""" 
    if not isinstance(a, int) or (a, float):
        raise TypeError("a must be an integer")
    """raise error if b is not an int or floar."""
    if not isinstance(b, int) or (b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
