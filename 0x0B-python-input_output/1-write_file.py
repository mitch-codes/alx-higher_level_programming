#!/usr/bin/python3
"""a function to write into files files"""


def write_file(filename="", text=""):
    """write content into file file in utf-8"""

    with open(filename, mode='w', encoding="UTF-8") as f:
        my_data = f.write(text)
        return my_data
