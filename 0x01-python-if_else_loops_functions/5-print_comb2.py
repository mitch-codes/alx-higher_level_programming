#!/usr/bin/python3
import sys
for i in range(100):
    if i < 10:
        print("0{:d}, ".format(i), end="")
    else:
        print("{:d}".format(i), end="")
        if i != 99:
            sys.stdout.write(", ")
sys.stdout.write("\n")
