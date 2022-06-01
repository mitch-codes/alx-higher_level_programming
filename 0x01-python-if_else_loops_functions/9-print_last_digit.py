#!/usr/bin/python3
def print_last_digit(number):
    mynumber = number
    length = len(str(mynumber))
    if mynumber < 0:
        mynumber = mynumber * -1
    for i in range(length - 1):
        mynumber = mynumber % 10
    return mynumber
