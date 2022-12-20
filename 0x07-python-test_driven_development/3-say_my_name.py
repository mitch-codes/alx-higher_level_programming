#!/usr/bin/python3
"""working with strings"""


def say_my_name(first_name, last_name=""):
    """Prints a string.
    Validates string inputs, the display
    the full name

    """
    if first_name == "":
        raise ValueError("first name must be specified")
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
