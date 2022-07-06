#!/usr/bin/python3
"""a function to write into files at the end of existing text"""


def append_write(filename="", text=""):
    """append content into file file in utf-8"""

    with open(filename, mode='a', encoding="UTF-8") as f:
        my_data = f.write(text)
        print(my_data)
        return my_data

