#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(length):
        digit = ord(str[i])
        if digit > 96 and digit < 123:
            digit = digit - 32
        print("{:c}".format(digit), end="")
    print("")
