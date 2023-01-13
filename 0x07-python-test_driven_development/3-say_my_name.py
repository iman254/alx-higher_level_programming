#!/usr/bin/python3

"""Function that prints the first and last name. """


def say_my_name(first_name, last_name=""):
    """ function that takes in first_name and last_name and prints them out.
    arg:
    first_name - first name to be input
    last_name - last name to be input """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
