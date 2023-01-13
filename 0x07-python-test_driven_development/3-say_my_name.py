#!/usr/bin/python3

"""Function that prints the first and last name.
def say_my_name(first_name, last_name=""):
    """ args:
    first_name - first name to be input
    last_name - last name to be input """


    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name == "":
        print(f"My name is {last_name}")
    elif first_name == "":
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")
