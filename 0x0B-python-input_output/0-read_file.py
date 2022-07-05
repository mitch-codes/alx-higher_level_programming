#!/usr/bin/python3
"""a method to read files"""


def read_file(filename=""):
    """read file in utf-8"""

    with open(filename, r, encoding="UTF-8") as f:
        my_data = f.read()
        print(my_data)
