#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    arguments = len(sys.argv) - 1
    if arguments == 1:
        print("{:d} argument:".format(arguments))
    else:
        print("{:d} arguments:".format(arguments))
    for i in range(1, length):
        print("{:d}: {}".format(i, sys.argv[i]))
