#!/usr/bin/python3
def max_integer(my_list=[]):
    max_number = 0
    for i in range(len(my_list)):
        if my_list[i] > max_number:
            max_number = my_list[i]
    return max_number
