#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    A function that prints x elements of a list.
    """
    list_count = 0
    for i in range(x):
        try:
            print(my_list[i])
            list_count += 1
        except IndexError:
            break
    return list_count
