#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return 0
    i = len(my_list) - 1
    while i > -1:
        print("{:d}".format(my_list[i]))
        i = i - 1
